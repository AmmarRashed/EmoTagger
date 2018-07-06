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


def get_emojis_dict(emojis_path="data/raw.txt"):
    emojis_dict = dict()  # {unicode: label}
    with open(emojis_path, 'r') as f:
        for line in f.readlines():
            tag, code = line.split("\t")
            emojis_dict[code.strip()] = tag
    return emojis_dict


# Emoticons


def get_emoticons_dict(url="https://pc.net/emoticons/"):
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



def save_data(save_dict=False):
    emojis_dict = get_emojis_dict()
    emoticons_dict = get_emoticons_dict()
    tags_dict = copy.deepcopy(emoticons_dict)
    tags_dict.update(emojis_dict)

    if save_dict:
        json.dump({"emojis": get_emojis_dict(), "emoticons": get_emoticons_dict()},
                  open("data/e_labels.json", "w"),
                  ensure_ascii=False)

    root = Node("")
    for emot, tag in tags_dict.items():
        add(root, emot, tag)

    pickle.dump(root, open("data/emoticons_trie.pkl", "wb"))

if __name__ == "__main__":
    save_data(True)