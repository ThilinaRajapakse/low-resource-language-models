import os
import pandas as pd
from tqdm.auto import tqdm
import re


data = []
for f in os.scandir("data/text_files"):
    with open(f, "r", encoding="utf-8") as t:
        text = t.readlines()
        text = ''.join([t for t in text if t])
        data.append(text)

with open("kikuyu_all.txt", "w", encoding="utf-8") as f:
    f.writelines(data)

# df = pd.read_csv("kikuyu/kik_community_2017-sentences.txt", sep='\t', header=None)

# df = df.iloc[:, 1]

# df.to_csv("kikuyu/kik_sentences_cleaned.txt", index=False, header=None)
