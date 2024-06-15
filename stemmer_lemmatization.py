# -*- coding: utf-8 -*-
"""
Created on Thus Jun 12 10:35:05 2024

@author: sai
"""

import nltk
nltk.download('punct')
from nltk import word_tokenize

#stemming
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programmed")
stemmer.stem("jumping")
stemmer.stem("jumped")

#####################################################
#lemmatizer 
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programmed")
lemmatizer.lemmatize("programs")
lemmatizer.lemmatize("battling")
lemmatizer.lemmatize("amazing")

###########################################################
#chunking(shallow parsing) identifying name entities
nltk.download("maxent_ne_chunker")
nltk.download('words')
sentence4="we are learning NLP in python by sanjivani"
#tokenize
nltk.download('averaged_perceptron_tagger')
words=word_tokenize(sentence4)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]


##############################################################
#sentence_tokenization
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("we are learning NLP in python.deliverd by sanjivani AI.located in kopargaon")
sent

###############################
#he went to bank and checked account was almost 0
#lloking this he went to river bank and was crying
from nltk.wsd import lesk
from nltk import word_tokenize
sentence1="keep your savings in the bank"
print(lesk(word_tokenize(sentence1),'banl'))

