import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

# Step 1: Define the POS tagging rules using regular expressions
patterns = [
    (r'.*ed$', 'VBD'),    # Verbs ending in 'ed' (past tense)
    (r'.*ing$', 'VBG'),   # Verbs ending in 'ing' (present participle)
    (r'\b(?:a|an|the)\b$', 'DT'),  # Determiners (a, an, the)
    (r'\b(?:he|she|it|they|I|we|you)\b$', 'PRP'),  # Pronouns
    (r'\b(?:quick|lazy|beautiful)\b$', 'JJ'),  # Adjectives (specific examples)
    (r'\b(?:and|but|or|nor)\b$', 'CC'),  # Conjunctions (and, but, or, nor)
    (r'\b(?:the)\b$', 'DT'),  # Article (the)
    (r'\b(?:run|eat|walk|jump)\b$', 'VB'),  # Example of verbs (use regular verb forms)
    (r'[A-Z][a-z]*$', 'NNP'),  # Proper Nouns (capitalized words)
    (r'\b(?:quick|fast|slow)\b$', 'JJ'),  # Example adjectives
    (r'\d+', 'CD'),  # Cardinal numbers
    (r'\s+', None),  # Skip spaces
    (r'\b(?:what|where|when|how)\b$', 'WP'),  # Question words (Wh-words)
]

# Step 2: Initialize the RegexpTagger with the defined patterns
tagger = RegexpTagger(patterns)

# Step 3: Test sentence
text = "The quick brown fox jumps over the lazy dog"

# Step 4: Tokenize the sentence
words = word_tokenize(text)

# Step 5: Apply POS tagging
tagged_words = tagger.tag(words)

# Step 6: Display the tagged words
print(tagged_words)
