import nltk
from nltk.tokenize import word_tokenize

# Ensure the required NLTK resources are downloaded
nltk.download('punkt')  # For word tokenization
nltk.download('averaged_perceptron_tagger')  # For POS tagging

# Function to perform POS tagging
def pos_tagging(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Perform part-of-speech tagging
    pos_tags = nltk.pos_tag(words)
    
    return pos_tags

# Example text
text = "NLTK is a great tool for text processing and analysis."

# Perform POS tagging
tagged_words = pos_tagging(text)

# Display the result
print("POS Tagging Result:")
for word, tag in tagged_words:
    print(f"{word}: {tag}")
