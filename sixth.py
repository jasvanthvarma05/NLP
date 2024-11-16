import nltk
from nltk.util import ngrams
from nltk import FreqDist

# Sample text (you can replace this with any text you want)
text = "This is a simple word prediction model that predicts the next word based on the previous one."

# Tokenize the text
tokens = nltk.word_tokenize(text.lower())  # Convert to lowercase to keep consistency

# Generate bigrams (2-grams)
bigrams = list(ngrams(tokens, 2))

# Calculate frequency distribution of bigrams
fdist = FreqDist(bigrams)

# Function to predict the next word given the current word
def predict_next_word(word, bigram_model):
    possible_bigrams = [(w1, w2) for (w1, w2) in bigram_model if w1 == word.lower()]
    return [w2 for (w1, w2) in possible_bigrams]

# Input word from user
input_word = input("Enter a word: ")

# Get the prediction
predictions = predict_next_word(input_word, bigrams)

# Display predictions
if predictions:
    print(f"Predictions for '{input_word}': {predictions}")
else:
    print(f"No prediction available for '{input_word}'.")
