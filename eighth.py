import nltk
from nltk.corpus import treebank
from nltk import FreqDist
from nltk.tag import UnigramTagger, BigramTagger

# Ensure you have the necessary NLTK datasets
nltk.download('treebank')
nltk.download('punkt')

# Step 1: Prepare training data
train_sents = treebank.tagged_sents()

# Step 2: Train a unigram POS tagger using the Treebank corpus
unigram_tagger = UnigramTagger(train_sents)

# Optionally, train a bigram POS tagger for better accuracy
bigram_tagger = BigramTagger(train_sents, backoff=unigram_tagger)

# Step 3: Test the POS tagger with a new sentence
test_sentence = "The quick brown fox jumps over the lazy dog".split()
tagged_sentence = bigram_tagger.tag(test_sentence)

# Step 4: Display the tagged sentence
print(tagged_sentence)
