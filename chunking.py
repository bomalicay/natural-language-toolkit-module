"""
This is based on the tutorial from this website: 
https://pythonprogramming.net/chunking-nltk-tutorial/
"""

# importing libraries
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer        # unsupervised machine learning tokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)      # training tokenizer first
tokenized = custom_sent_tokenizer.tokenize(sample_text)

# processing content
def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            chunked.draw()

    except Exception as e:
        print(str(e))

process_content()

# check POS tag list text file to compare output