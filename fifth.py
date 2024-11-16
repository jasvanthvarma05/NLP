import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
def stemmin(input):
    words = word_tokenize(input)
    porter = [PorterStemmer().stem(word) for word in words]
    print(porter) 
wordsi = "Running and played are both verb forms of the word run and play."
result = stemmin(wordsi)
print(result)