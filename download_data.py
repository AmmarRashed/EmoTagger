# Emojis

import re, json, copy, pickle
import urllib.request as ureq
from bs4 import BeautifulSoup
from Trie import *


def clean_code_label(code, label):
    codes = list()
    labels = list()
    splitted_codes = code.split("..")
    splitted_labels = label.split("..")
    for i in range(len(splitted_codes)):
        codes.append(splitted_codes[i])
        labels.append(splitted_labels[i])
    return codes, labels


def get_emojis_dict(emojis_path="emojis.txt"):
    with open("data/emojis.txt", 'r') as f:
        emojis_raw = f.read()

    emojis_dict = dict()  # {unicode: label}
    for l in emojis_raw.split("\n"):
        if "; Emoji" in l:
            emoji_info = re.findall(r"\)\s+[A-Za-z]+.+", l)
            try:
                emoji_info[0]
            except IndexError:
                continue
            else:
                label_raw = re.sub("\)\s+", "", emoji_info[0])
                code_raw = l.split()[0]

                codes, labels = clean_code_label(code_raw, label_raw)
                for i in range(len(codes)):
                    emojis_dict[codes[i]] = labels[i]
    return emojis_dict

# Emoticons


def download_emoticons(url="https://pc.net/emoticons/"):
    opener = ureq.FancyURLopener({})
    f = opener.open(url)
    content = f.read()
    soup = BeautifulSoup(content, "html")
    emoticons_html_tags = soup.find_all(class_="smiley")

    emoticons_dict = dict()
    for t in emoticons_html_tags:
        label = t.a.attrs["href"].split("/")[1]
        emoticons_dict[t.text] = label
    return emoticons_dict



def save_data():
    emojis_dict = get_emojis_dict()
    emoticons_dict = download_emoticons()
    tags_dict = copy.deepcopy(emoticons_dict)
    tags_dict.update(emojis_dict)

    root = Node("")
    for emot, tag in tags_dict.items():
        add(root, emot, tag)

    pickle.dump(root, open("data/emoticons_trie.pkl", "wb"))

if __name__ == "__main__":
    save_data()

# json.dump({"emojis":emojis_dict, "emoticons":emoticons_dict},
#           open("e_labels.json","w"),
#           ensure_ascii=False)