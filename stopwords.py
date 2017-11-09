"""
This is based on the tutorial from this website: 
https://pythonprogramming.net/stop-words-nltk-tutorial/
"""
# importing libraries
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# using stopwords
stop_words = set(stopwords.words("english"))
print(stop_words)       # show list of words in stop_words

words = word_tokenize(sample_text)

filtered_words = []
for w in words:
    if w not in stop_words:
        filtered_words.append(w)

# or use this one-liner as an alternative

filtered_words = [w for w in words if not w in stop_words]

print(filtered_words)