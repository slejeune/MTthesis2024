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

# fr <-> ig
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/fra_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/ibo_Latn.dev",
        "French", "Igbo")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/ibo_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/fra_Latn.dev",
        "Igbo", "French")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/fr-ig/NLLB.fr-ig.fr",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/fr-ig/NLLB.fr-ig.ig",
        "French", "Igbo")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/fr-ig/NLLB.fr-ig.ig",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/fr-ig/NLLB.fr-ig.fr",
        "Igbo", "French")



# nl <-> li
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/lim_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/nld_Latn.dev",
        "Limburgish", "Dutch")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/nld_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/lim_Latn.dev",
        "Dutch", "Limburgish")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/nl-li/NLLB.nl-li.li",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/nl-li/NLLB.nl-li.nl",
        "Limburgish", "Dutch")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/nl-li/NLLB.nl-li.nl",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/nl-li/NLLB.nl-li.li",
        "Dutch", "Limburgish")
# Wikimedia
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Wikimedia/nl-li/wikimedia.li-nl.li",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Wikimedia/nl-li/wikimedia.li-nl.nl",
        "Limburgish", "Dutch")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Wikimedia/nl-li/wikimedia.li-nl.nl",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Wikimedia/nl-li/wikimedia.li-nl.li",
        "Dutch", "Limburgish")

# jp <-> ne
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/npi_Deva.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/jpn_Jpan.dev",
        "Nepali", "Japanese")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/jpn_Jpan.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/npi_Deva.dev",
        "Japanese", "Nepali")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ja-ne/NLLB.ja-ne.ja",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ja-ne/NLLB.ja-ne.ne",
        "Japanese", "Nepali")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ja-ne/NLLB.ja-ne.ne",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/ja-ne/NLLB.ja-ne.ja",
        "Nepali", "Japanese")

# tg <-> cy
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/tgl_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/cym_Latn.dev",
        "Tagalog", "Welsh")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/cym_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/flores_subset/dev/tgl_Latn.dev",
        "Welsh", "Tagalog")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/tl-cy/NLLB.tl-cy.tl",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/tl-cy/NLLB.tl-cy.cy",
        "Tagalog", "Welsh")
extract("/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/tl-cy/NLLB.tl-cy.cy",
        "/Users/Suzenator/Documents/Uni/M4/MThesis/Data/Non-English-preprocessed/tl-cy/NLLB.tl-cy.tl",
        "Welsh", "Tagalog")


random.shuffle(res)

outfile = open("NLLB-flores200_dev.high_low.json", "w")
json.dump(res, outfile, ensure_ascii=False, indent=2)
