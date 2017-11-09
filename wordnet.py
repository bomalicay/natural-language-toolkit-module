"""
This is based on the tutorial from this website: 
https://pythonprogramming.net/wordnet-nltk-tutorial/
"""

# importing libraries
from nltk.corpus import wordnet

syns = wordnet.synsets("program")       # get synonyms of a specified word

print(syns)                             # list
print(syns[0].lemmas()[0].name())       # showing just the word of a specified element
print(syns[0].definition())             # showing the definition of a specified element
print(syns[0].examples())               # shows sample statements using a specified element

# display synonyms and antonyms
synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

# return percentage of similarity
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cat.n.01")
print(w1.wup_similarity(w2))