import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Download necessary NLTK resources (if not already installed)
nltk.download('punkt')

# Define the Context-Free Grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'mat' | 'telescope'
    V -> 'saw' | 'sat'
    P -> 'on' | 'with'
""")

# Create a parser
parser = ChartParser(grammar)

# Define the sentence to be parsed
sentence = "the cat saw the dog".split()

# Generate the parse tree for the sentence
for tree in parser.parse(sentence):
    tree.pretty_print()  # This will print the parse tree in the console
    break  # Stops after generating the first parse tree
