# EmoticonTrieTagger
Detecting emoticons with a Trie implementation and generating the tagged text.

## Data
<p><a href="https://pc.net/emoticons/"> Emoticons </a></p>
<p><a href="https://unicode.org/Public/emoji/11.0/emoji-data.txt"> Emojis </a></p>

## Usage

```bash
$ python3.5 emoticons.py "hello :). I am very happy to meet you xD"
>>> Tagged text saved to out.txt
>>> Print the tagged text (Y or N)?
$ Y
>>> hello <emoticon type=smile>:).</emoticon> I am very happy to meet you <emoticon type=laughing>xD</emoticon>
```
