import spacy
nlp = spacy.load("en_core_web_sm")
text = "This is the first sentence. Here's the second one!"
doc = nlp(text)
for sent in doc.sents:
    print(sent.text)
