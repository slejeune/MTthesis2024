#!/bin/bash

strindex() { 
  x="${1%%"$2"*}"
  [[ "$x" = "$1" ]] && echo -1 || echo "${#x}"
}

# Variables for the experiment scenario
SCENARIO=low_low  # Options: low_low, high_low, high_high
SVORZH=supervised # Options: supervised, zeroshot
ALPHA=0
PROMPT=gpt-mt

# Paths and folders
COMETCKPT=wmt22-comet-da/checkpoints/model.ckpt
DATAFOLDER=~/MThesis/CrossConST-LLM/dataset/flores_subset/devtest
RESFOLDER=~/MThesis/CrossConST-LLM/output/${SCENARIO}/${ALPHA}_${PROMPT}/${SVORZH}
OUT=~/MThesis/CrossConST-LLM/output/eval/eval_${SCENARIO}_${SVORZH}_${ALPHA}_${PROMPT}.txt

# Define language codes
declare -A LANG_CODES
LANG_CODES=( ["fra"]="fra_Latn" ["ibo"]="ibo_Latn" ["jpn"]="jpn_Jpan" ["lim"]="lim_Latn"
             ["nld"]="nld_Latn" ["cym"]="cym_Latn" ["npi"]="npi_Deva" ["tgl"]="tgl_Latn"
             ["ces"]="ces_Latn" ["deu"]="deu_Latn" ["gle"]="gle_Latn" ["pan"]="pan_Guru"
             ["rus"]="rus_Cyrl" ["zho"]="zho_Hans" ["sag"]="sag_Latn" ["ltz"]="ltz_Latn" )

# Define language pairs for each scenario and case
declare -A PAIRS

# low_low scenario
PAIRS["low_low_supervised"]="ibo-lim ibo-npi ibo-cym lim-npi lim-cym npi-cym"
PAIRS["low_low_zero-shot"]="lim-ltz lim-pan ibo-ltz ibo-sag npi-pan npi-gle cym-gle cym-sag"

# high_low scenario
PAIRS["high_low_supervised"]="fra-ibo nld-lim jpn-npi tgl-cym"
PAIRS["high_low_zero-shot"]="fra-lim fra-npi fra-cym nld-ibo nld-npi nld-cym jpn-ibo jpn-lim jpn-cym tgl-ibo tgl-lim tgl-npi"

# high_high scenario
PAIRS["high_high_supervised"]="fra-nld fra-jpn fra-tgl nld-jpn nld-tgl jpn-tgl"
PAIRS["high_high_zero-shot"]="nld-deu fra-ces jpn-zho tgl-rus nld-zho fra-deu jpn-rus tgl-ces"

# Helper function to add reverse pairs
add_reverse_pairs() {
  local pairs="$1"
  local new_pairs=""
  for pair in $pairs; do
    local src_lang=${pair%-*}
    local tgt_lang=${pair#*-}
    new_pairs+="$pair ${tgt_lang}-${src_lang} "
  done
  echo $new_pairs
}

# Select the correct pairs based on scenario and case
SELECTED_PAIRS=$(add_reverse_pairs "${PAIRS["${SCENARIO}_${SVORZH}"]}")

# Initialize output file
echo "BLEU/chrF/COMET" > "$OUT"

# Loop through selected pairs for the chosen scenario and case
for PAIR in $SELECTED_PAIRS; do
  # Split language codes by '-'
  SRC_LANG=${PAIR%-*}
  TGT_LANG=${PAIR#*-}
  
  SRC_CODE=${LANG_CODES[$SRC_LANG]}
  TGT_CODE=${LANG_CODES[$TGT_LANG]}

  # Define paths
  SRC=${DATAFOLDER}/${SRC_CODE}.devtest
  HYP=${RESFOLDER}/${SRC_CODE}.devtest.${SRC_LANG}2${TGT_LANG}_translation
  REF=${DATAFOLDER}/${TGT_CODE}.devtest

  # Calculate BLEU score
  BLEU=$(sacrebleu -tok 13a "${REF}" < "${HYP}" | jq '.score')

  # Calculate chrF score
  chrF=$(sacrebleu -m chrf -tok 13a "${REF}" < "${HYP}" | jq '.score')

  # Calculate COMET score
  COMET=$(python3 compute_comet.py --file_src "${SRC}" --file_hyp "${HYP}" --file_ref "${REF}" | grep -oP '(?<=COMET Score is )[-+]?[0-9]*\.?[0-9]+')

  # Check for missing scores
  if [[ -z "$BLEU" ]]; then BLEU="N/A"; fi
  if [[ -z "$chrF" ]]; then chrF="N/A"; fi
  if [[ -z "$COMET" ]]; then COMET="N/A"; fi

  # Output to file
  echo "${SRC_LANG}-${TGT_LANG} ${BLEU}/${chrF}/${COMET}" >> "$OUT"
done
