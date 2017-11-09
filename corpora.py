"""
This is based on the tutorial from this website: 
https://pythonprogramming.net/nltk-corpus-corpora-tutorial/
"""

# importing libraries
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

sample = gutenberg.raw("shakespeare-hamlet.txt")

tok = sent_tokenize(sample)

print(tok[5:15])