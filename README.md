# EmoTagger
<p>
<img src="https://cdn.shopify.com/s/files/1/1061/1924/products/Emoji_Icon_-_Sunglasses_cool_emoji_large.png?v=1513251060" width=100 /></br>
Detecting emoticons with a Trie implementation and generating the tagged text.
  </p>
  
## Data

<p><a href="https://pc.net/emoticons/"> Emoticons </a></p>
<p><a href="https://github.com/uclmr/emoji2vec/blob/master/data/raw_training_data/emoji_joined.txt"> Emojis </a></p>

## Usage

```bash
$ python3.5 emoticons.py "hello :). I am very happy to meet you xD"
>>> Tagged text saved to out.txt
>>> Print the tagged text (Y or N)?
$ Y
>>> hello <emoticon type=smile>:).</emoticon> I am very happy to meet you <emoticon type=laughing>xD</emoticon>
```
