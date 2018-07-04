import unittest, json, random, string
from emoticons import generate_tagged_text

class EmoticonTest(unittest.TestCase):
    data = json.load(open("e_labels.json","r"))
    tags_dict = data["emoticons"]
    tags_dict.update(data["emojis"])  # {emoticon: tag}
    maxDiff = None

    def is_emot(self, txt:str):
        is_emot = False
        if txt in self.tags_dict:
            is_emot = True
        else:
            for t in self.tags_dict:
                if t in txt and t[0] == txt[0]:
                    is_emot = True
        return is_emot

    def test(self):
        for k in range(500):
            raw = ""
            tagged = ""
            for i in range(100):
                raw += ' '
                tagged += ' '

                if random.random()<0.5:
                    while 1:
                        txt = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(3,8)))
                        if not (self.is_emot(txt.upper()) or self.is_emot(txt)):
                            break

                    raw += txt
                    tagged += txt
                else:
                    emoticon = random.choice(list(self.tags_dict.keys()))
                    tag = self.tags_dict[emoticon]

                    raw += emoticon
                    tagged += "<emoticon type=%s>%s</emoticon>"%(tag, emoticon)

            raw = raw.strip()
            tagged = tagged.strip()

            self.assertEqual(generate_tagged_text(raw), tagged)


if __name__ == '__main__':
    unittest.main()