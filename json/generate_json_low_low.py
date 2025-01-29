import json
import random


def extract(file_src, file_tgt, src, tgt):

    lines_src = open(file_src, 'r').readlines()
    lines_tgt = open(file_tgt, 'r').readlines()

    assert len(lines_src) == len(lines_tgt)

    for i in range(len(lines_src)):
        tmp = {}
        tmp["input"] = lines_src[i].strip()
        tmp["input_lang"] = src
        tmp["output"] = lines_tgt[i].strip()
        tmp["output_lang"] = tgt
        res.append(tmp)
    return


res = []

# ne <-> ib
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/npi_Deva.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/ibo_Latn.dev",
        "Nepali", "Igbo")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/ibo_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/npi_Deva.dev",
        "Igbo", "Nepali")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ne-ig/NLLB.ne-ig.ne",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ne-ig/NLLB.ne-ig.ig",
        "Nepali", "Igbo")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ne-ig/NLLB.ne-ig.ig",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ne-ig/NLLB.ne-ig.ne",
        "Igbo", "Nepali")

# ne <-> cy
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/npi_Deva.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/cym_Latn.dev",
        "Nepali", "Welsh")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/cym_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/npi_Deva.dev",
        "Welsh", "Nepali")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ne-cy/NLLB.ne-cy.ne",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ne-cy/NLLB.ne-cy.cy",
        "Nepali", "Welsh")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ne-cy/NLLB.ne-cy.cy",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ne-cy/NLLB.ne-cy.ne",
        "Welsh", "Nepali")

# ne <-> li
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/npi_Deva.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/lim_Latn.dev",
        "Nepali", "Limburgish")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/lim_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/npi_Deva.dev",
        "Limburgish", "Nepali")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ne-li/NLLB.ne-li.ne",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ne-li/NLLB.ne-li.li",
        "Nepali", "Limburgish")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ne-li/NLLB.ne-li.li",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ne-li/NLLB.ne-li.ne",
        "Limburgish", "Nepali")

# ib <-> cy
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/ibo_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/cym_Latn.dev",
        "Igbo", "Welsh")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/cym_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/ibo_Latn.dev",
        "Welsh", "Igbo")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ig-cy/NLLB.ig-cy.ig",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ig-cy/NLLB.ig-cy.cy",
        "Igbo", "Welsh")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ig-cy/NLLB.ig-cy.cy",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ig-cy/NLLB.ig-cy.ig",
        "Welsh", "Igbo")

# ib <-> li
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/ibo_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/lim_Latn.dev",
        "Igbo", "Limburgish")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/lim_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/ibo_Latn.dev",
        "Limburgish", "Igbo")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ig-li/NLLB.ig-li.ig",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ig-li/NLLB.ig-li.li",
        "Igbo", "Limburgish")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ig-li/NLLB.ig-li.li",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ig-li/NLLB.ig-li.ig",
        "Limburgish", "Igbo")

# cy <-> li
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/lim_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/cym_Latn.dev",
        "Limburgish", "Welsh")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/cym_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/lim_Latn.dev",
        "Welsh", "Limburgish")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/cy-li/NLLB.cy-li.li",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/cy-li/NLLB.cy-li.cy",
        "Limburgish", "Welsh")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/cy-li/NLLB.cy-li.cy",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/cy-li/NLLB.cy-li.li",
        "Welsh", "Limburgish")


random.shuffle(res)

outfile = open("NLLB-flores200_dev.low_low.json", "w")
json.dump(res, outfile, ensure_ascii=False, indent=2)
