import argparse
import io
import pickle
import os

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM
from transformers import LlamaTokenizer

import numpy as np
import pandas as pd

from tqdm import tqdm
from tqdm import trange


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fin', required=False)
    parser.add_argument('--ckpt', required=True)
    parser.add_argument('--src', required=False)
    parser.add_argument('--tgt', required=False)
    parser.add_argument('--prompt', required=True)
    return parser


parser = get_parser()
args = parser.parse_args()

# Extract model name from the checkpoint path
model_name = os.path.basename(args.ckpt).split('.')[0]

print(f'Evaluating for model "{model_name}"')

nl = r"dataset/flores_subset/devtest/nld_Latn.devtest"
fr = r"dataset/flores_subset/devtest/fra_Latn.devtest"
jp = r"dataset/flores_subset/devtest/jpn_Jpan.devtest"
tg = r"dataset/flores_subset/devtest/tgl_Latn.devtest"
lang_locs = [nl, fr, jp, tg]

languages = ["Dutch", "French", "Japanese", "Tagalog"]
languages_short = ["nl", "fr", "jp", "tg"]

base_model = AutoModelForCausalLM.from_pretrained("haoranxu/ALMA-13B-Pretrain", torch_dtype=torch.float16, device_map="auto")
model = PeftModel.from_pretrained(base_model, args.ckpt)
model.eval()
tokenizer = LlamaTokenizer.from_pretrained("haoranxu/ALMA-13B-Pretrain", padding_side='left')

languages_hidden_states = {lang: [] for lang in languages_short}

print("Now starting inference.")

for i in trange(len(languages), desc="Processing languages"):
    prompt_list = []
    lang_code = languages_short[i]
    lang_hidden_states = []  # Temporary storage for this language's hidden states

    # Preprocess prompts
    with open(lang_locs[i], 'r') as f:
        lines = f.readlines()

    for line in lines:
        if args.prompt == "gpt-mt":
            prompt = "Translate this from {} to {}:\n{}: {}\n{}:".format(
                languages[i], "French", languages[i], line.strip(), "French")
        elif args.prompt == "t-enc":
            prompt = "{}: {}\n".format("French", line.strip())
        elif args.prompt == "t-dec":
            prompt = "{}\n{}:".format(line.strip(), "French")
        elif args.prompt == "s-enc-t-enc":
            prompt = "{} {}: {}\n".format(languages[i], "French", line.strip())
        elif args.prompt == "s-enc-t-dec":
            prompt = "{}: {}\n{}:".format(languages[i], line.strip(), "French")

        prompt_list.append(prompt)

    # Get hidden states, one sentence at a time
    for input in tqdm(prompt_list, desc=f"Processing prompts for {languages[i]}"):
        input_ids = tokenizer(input, return_tensors="pt", padding=True, max_length=256, truncation=True).input_ids.cuda()

        with torch.no_grad():
            generated_ids = model.generate(
                input_ids=input_ids,
                num_beams=5,
                do_sample=False,
                max_new_tokens=256,
                output_hidden_states=True,
                return_dict_in_generate=True
            )

        hidden = generated_ids.hidden_states[-1][-1][0]  # Last token, last transformer layer, first (/best) beam
        lang_hidden_states.append(hidden)

    # Save hidden states for the current language
    individual_file = f"hidden_states/hidden_{lang_code}_fr_{model_name}.txt"
    with open(individual_file, "wb") as f:
        pickle.dump(lang_hidden_states, f)

    print(f"Saved hidden states for {languages[i]} to {individual_file}")

    # Add to the full dictionary
    languages_hidden_states[lang_code] = lang_hidden_states

# Save full pickle file with all languages
full_file = f"hidden_states/hidden_full_HH_sv_{model_name}.txt"
with open(full_file, "wb") as f:
    pickle.dump(languages_hidden_states, f)

print(f"Saved combined hidden states for all languages to {full_file}")
