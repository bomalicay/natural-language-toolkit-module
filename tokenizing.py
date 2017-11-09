"""
This is based on the tutorial from this website: 
https://pythonprogramming.net/tokenizing-words-sentences-nltk-tutorial/
"""
# importing libraries
from nltk.tokenize import sent_tokenize, word_tokenize

sample_text = "Hello world. Nice weather we're having. How are you doing today? Please don't be scared by Python, it's just a language."
print(sent_tokenize(sample_text))       # separating by sentences
print(word_tokenize(sample_text))       # separating by words