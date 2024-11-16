import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import CFG

# Download necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Define a simple grammar for parsing
grammar = """
  S -> NP VP
  NP -> DT NN
  VP -> VBZ NP
  DT -> 'The' | 'a'
  NN -> 'dog' | 'cat'
  VBZ -> 'barks' | 'runs'
"""

# Initialize the CFG parser
parser = nltk.ChartParser(nltk.CFG.fromstring(grammar))

# Example sentence
sentence = "The dog barks"

# Tokenize the sentence
tokens = word_tokenize(sentence)

# POS tagging the tokens
tagged_tokens = pos_tag(tokens)

# Parse the sentence using the grammar
for tree in parser.parse(tokens):
    tree.draw()  # Opens a window with the tree visualization
