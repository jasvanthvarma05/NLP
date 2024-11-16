import nltk
from nltk import CFG

# Define the grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'a' | 'the'
    N -> 'man' | 'dog' | 'cat'
    V -> 'saw' | 'ate'
    P -> 'with'
""")

# Function to check sentence
def check_sentence(sentence):
    words = sentence.lower().split()
    parser = nltk.ChartParser(grammar)

    # Try parsing the sentence
    try:
        for tree in parser.parse(words):
            print(tree)  # Print the parse tree
            return True  # If a tree is found, the sentence is grammatical
    except ValueError:
        pass

    return False  # If no tree is found

# Main function
def main():
    sentence = input("Enter a sentence: ")

    if check_sentence(sentence):
        print("The sentence is grammatically correct.")
    else:
        print("The sentence is not grammatically correct.")

# Entry point
if __name__ == "__main__":
    main()
