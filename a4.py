import nltk
from nltk.util import ngrams

sentence = "I Love Natural Language Processing"

word = nltk.word_tokenize(sentence)

bigrams = list(ngrams(word,2))
print(f"Bigrams : {bigrams}")

trigrams = list(ngrams(word,3))
print(f"Trigrams : {trigrams}")