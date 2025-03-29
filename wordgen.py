from nltk.util import ngrams
from nltk.lm.preprocessing import padded_everygram_pipeline # wtf does this mean halp
from nltk.lm import KneserNeyInterpolated
import sys
from random import sample
print(sys.getdefaultencoding())
# sys.setdefaultencoding("utf-8")


# https://freedium.cfd/https://medium.com/@vsagziyagli/text-generation-using-n-grams-ef49e6e43d39

wordlist = []
with open("data/data.txt", "r", encoding="utf-8") as dunmeris:
    # ald
    wordlist = [word.strip() for word in dunmeris.readlines()]

text = " ".join(sample(wordlist, len(wordlist)))
print(text)
n = 3

train, vocab = padded_everygram_pipeline(n, text.split())
model = KneserNeyInterpolated(n) 
model.fit(train, vocab)
# print(model.generate(num_words = 10, random_seed=5283475))
print(model.generate(num_words = 10))

