import pickle, copy, sys


def get_emoticon_tag(token:str):
    node = root
    tag = None

    for i in range(len(token)):
        char = token[i]
        in_children = False
        for c in node.children:
            if char == c.char:
                node = c
                tag = node.tag
                in_children = True
                break
        if not in_children:
            break
    return tag


def generate_tagged_text(text:str):
    generate_tag = lambda tag,emoticon: "<emoticon type={}>{}</emoticon>".format(tag,emoticon)
    tokens = text.split()

    tagged_tokens = copy.deepcopy(tokens)
    for i,token in enumerate(tokens):
        tag = get_emoticon_tag(token.upper())  # Emojis codes are all upper case
        if tag:
            tagged_tokens[i] = generate_tag(tag, token)
        else:
            tag = get_emoticon_tag(token)
            if tag:
                tagged_tokens[i] = generate_tag(tag, token)
    return " ".join(tagged_tokens)


try:
    root = pickle.load(open("data/emoticons_trie.pkl", "rb"))
except:
    from download_data import save_data
    save_data()
    root = pickle.load(open("data/emoticons_trie.pkl", "rb"))


if __name__ == '__main__':
    program = sys.argv[0]
    emoticon_text = sys.argv[1]
    tagged_text = generate_tagged_text(emoticon_text)
    with open("out.txt","w") as f:
        f.write(tagged_text)
    print("Tagged text saved to out.txt")
    p = input("Print the tagged text (Y or N)? ")
    if "Y" in p:
        print(tagged_text)
