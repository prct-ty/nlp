from nltk.corpus import wordnet
import nltk

nltk.download('wordnet')

word1 = "dog"
word2 = "cat"

syn1 = wordnet.synsets(word1)
syn2 = wordnet.synsets(word2)

if syn1 and syn2:
    similarity = wordnet.wup_similarity(syn1[0], syn2[0])
    print(f"Similarity between {word1} and {word2}: {similarity}")
else:
    print("One or both words do not have synsets in WordNet.")

same1 = []
diff1 = []

for syn in syn1:
    for word in syn.lemmas():
        same1.append(word.name())

        if word.antonyms():
            diff1.append(word.antonyms()[0].name())

print("\nSynonyms (same):")
for words in same1[:5]:
    print(words)

print("\nAntonyms (diff):")
for words in diff1[:5]:
    print(words)
