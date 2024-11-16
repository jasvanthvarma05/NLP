import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')

text = "John went to the store. He bought some milk."
tagged = [nltk.pos_tag(nltk.word_tokenize(s)) for s in nltk.sent_tokenize(text)]
resolved = ' '.join(w if w.lower() != 'he' else tagged[0][0][0] for sent in tagged for w, t in sent)

print("Original:", text)
print("Resolved:", resolved)