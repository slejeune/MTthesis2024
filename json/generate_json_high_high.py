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

# fr <-> jp
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/fra_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/jpn_Jpan.dev",
        "French", "Japanese")
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/jpn_Jpan.dev",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/fra_Latn.dev",
        "Japanese", "French")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/fr-ja/NLLB.fr-ja.fr",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/fr-ja/NLLB.fr-ja.ja",
        "French", "Japanese")
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/fr-ja/NLLB.fr-ja.ja",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/fr-ja/NLLB.fr-ja.fr",
        "Japanese", "French")



# fr <-> nl
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/fra_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/nld_Latn.dev",
        "French", "Dutch")
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/nld_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/fra_Latn.dev",
        "Dutch", "French")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/fr-nl/NLLB.fr-nl.fr",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/fr-nl/NLLB.fr-nl.nl",
        "French", "Dutch")
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/fr-nl/NLLB.fr-nl.nl",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/fr-nl/NLLB.fr-nl.fr",
        "Dutch", "French")

# fr <-> tg
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/fra_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/tgl_Latn.dev",
        "French", "Tagalog")
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/tgl_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/fra_Latn.dev",
        "Tagalog", "French")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/fr-tl/NLLB.fr-tl.fr",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/fr-tl/NLLB.fr-tl.tl",
        "French", "Tagalog")
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/fr-tl/NLLB.fr-tl.tl",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/fr-tl/NLLB.fr-tl.fr",
        "Tagalog", "French")

# jp <-> nl
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/jpn_Jpan.dev",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/nld_Latn.dev",
        "Japanese", "Dutch")
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/nld_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/jpn_Jpan.dev",
        "Dutch", "Japanese")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/ja-nl/NLLB.ja-nl.ja",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/ja-nl/NLLB.ja-nl.nl",
        "Japanese", "Dutch")
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/ja-nl/NLLB.ja-nl.nl",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/ja-nl/NLLB.ja-nl.ja",
        "Dutch", "Japanese")

# jp <-> tg
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/jpn_Jpan.dev",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/tgl_Latn.dev",
        "Japanese", "Tagalog")
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/tgl_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/jpn_Jpan.dev",
        "Tagalog", "Japanese")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/ja-tl/NLLB.ja-tl.ja",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/ja-tl/NLLB.ja-tl.tl",
        "Japanese", "Tagalog")
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/ja-tl/NLLB.ja-tl.tl",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/ja-tl/NLLB.ja-tl.ja",
        "Tagalog", "Japanese")

# nl <-> tg
# FLORES-200
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/nld_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/tgl_Latn.dev",
        "Dutch", "Tagalog")
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/tgl_Latn.dev",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/flores_subset/dev/nld_Latn.dev",
        "Tagalog", "Dutch")
# NLLB
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/tl-nl/NLLB.tl-nl.nl",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/tl-nl/NLLB.tl-nl.tl",
        "Dutch", "Tagalog")
extract("/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/tl-nl/NLLB.tl-nl.tl",
        "/Users/Suzenator/Documents/Uni/M4/Doshisha M Thesis/Data/Non-English-preprocessed/tl-nl/NLLB.tl-nl.nl",
        "Tagalog", "Dutch")


random.shuffle(res)

outfile = open("NLLB-flores200_dev.fr_nl_jp_tg.json", "w")
json.dump(res, outfile, ensure_ascii=False, indent=2)
