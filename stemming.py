"""
This is based on the tutorial from this website: 
https://pythonprogramming.net/stemming-nltk-tutorial/
"""

# importing libraries
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

sample_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

for w in sample_words:
    print(ps.stem(w))

sample_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(sample_text)

for w in words:
    print(ps.stem(w))