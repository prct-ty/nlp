from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

sentence = "The players were running happily in the kindness of the community."

tokens = word_tokenize(sentence)

add = [("play", "player"), ("kind", "kindness"), ("happy", "unhappy")]
print("Add Table:")
for base, new in add:
    affix = new.replace(base, "")
    print(f"{base} + {affix} = {new}")

delete = tokens
print("\nDelete Table (Using Stemming):")
for word in delete:
    stemmed_word = stemmer.stem(word)
    print(f"{word} -> {stemmed_word}")

