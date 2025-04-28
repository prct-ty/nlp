import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "The quick brown fox jumps over the lazy dog"

words = nltk.word_tokenize(sentence)

pos_tags = nltk.pos_tag(words)

for word, tags in pos_tags:
    print(f"{word} -> {tags}")