import spacy

nlp = spacy.load("en_core_web_sm")

text = "Utkarsh Pingale was born on 8:30 am in Pune and go to AISSMSIOIT college"

doc = nlp(text)

for word in doc:
    if word.ent_type_:
        print(f"{word.text:<15} -> {word.ent_type_}")
    else:
        print(f"{word.text:<15} -> None")

print()
for word in doc.ents:
    print(f"{word.text:<15} : {word.label_}")

# ----------------------------------------------------------------------

import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

text = "Utkarsh Pingale was born on 8:30 am in Pune and go to AISSMSIOIT college"

tokens = word_tokenize(text)
tags = pos_tag(tokens)

entities = ne_chunk(tags)

for chunk in entities:
    if isinstance(chunk, nltk.Tree):
        print(f"{' '.join([word for word, tag in chunk])} -> {chunk.label()}")
    else:
        print(f"{chunk[0]} -> None")
