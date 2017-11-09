"""
This is based on the tutorial from this website: 
https://pythonprogramming.net/lemmatizing-nltk-tutorial/
"""

# importing libraries
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))

# Note: The default parameter fot lemmatize is pos="n".

"""
output:
cat
cactus
goose
rock
python
better
good
best
"""