"""
This is based on the tutorial from this website: 
https://pythonprogramming.net/text-classification-nltk-tutorial/
"""

# importing libraries
import nltk
import random
from nltk.corpus import movie_reviews

documents = []
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append(list(movie_reviews.words(fileid)), category)

"""
# one-liner version
documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
"""

random.shuffle(documents)
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))        # display top 15 most common words
print(all_words["stupid"])              # display how many times a specified word appear