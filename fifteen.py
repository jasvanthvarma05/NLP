import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

# Define the grammar
grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.7] | V NP PP [0.3]
    V -> 'saw' [1.0]
    NP -> 'John' [0.5] | 'Mary' [0.5]
    PP -> P NP [1.0]
    P -> 'with' [1.0]
""")

# Create a Viterbi parser
viterbi_parser = ViterbiParser(grammar)

# Define the sentence to parse
sentence = ['John', 'saw', 'Mary']

# Parse the sentence and display the parse tree(s)
for tree in viterbi_parser.parse(sentence):
    print(tree)
    tree.pretty_print()