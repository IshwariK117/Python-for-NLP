# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:25:59 2024

@author: sai
"""
## Python for NLP ##

####### Text Mining #########
sentence="we are learning textMining from sanjivani AI"
sentence.index("learning")
#Output : 7
#it shows output based on w=0,e=1,'(space)'=2....L=7

####################################################
sentence.split().index("textMining")
#output:3
#it first split the sentence into words and give output as 
#we=0,are=1,learning=2,textMining=3
#its doing tokenization

####################################################

#reversing the string 
sentence.split()[2][::-1]
#[start:end:-1(start fro last word)] 
#output:'gninrael'

####################################################

words=sentence.split() #tokenization
first_word=words[0]
first_word
last_word=words[-1]
last_word
#concatenate fist and last word
concat_word=first_word+" "+last_word
concat_word

####################################################

#print even words from the sentence
[words[i] for i in range(len(words)) if i%2==0]
#Out[24]: ['we', 'learning', 'from', 'AI']

#display only certain word like AI
sentence[-3:]
#Out[30]: ' AI'            extract words from end

#all sentence in reverse order
sentence[::-1]
#Out[31]: 'IA inavijnas morf gniniMtxet gninrael era ew'

#select each word and print in reverse order
words
print( " ".join(word[::-1] for word in words))
#output:ew era gninrael gniniMtxet morf inavijnas IA

####################################################

import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize("I am reading NLP fundamentals")
print(words)
#['I', 'am', 'reading', 'NLP', 'fundamentals']

####################################################
#part of speech (PoS) tagging
nltk.download('averaged_perceptron_tagger') #dont mistakje in spelling
nltk.pos_tag(words)
"""
Out[49]: 
[('I', 'PRP'),
 ('am', 'VBP'),
 ('reading', 'VBG'),
 ('NLP', 'NNP'),
 ('fundamentals', 'NNS')]
"""

###################################################
#stop words from nltk library
import nltk
from nltk.corpus import stopwords
# Download the stopwords
nltk.download('stopwords')
# Get the English stop words
stop_words = stopwords.words('english')
print(stop_words)
# Example sentence
sentence = "I am learning NLP it is one of the most used."


#######################################################
#replace word or short forms in another word or strings
sentence2="I visited my IND on 14-02-19"
normalised_sentence=sentence2.replace("my","Malaysia").replace("IND","India")
normalised_sentence=normalised_sentence.replace("-19","-2020")
print(normalised_sentence)
#output:I visited Malaysia India on 14-02-2020
#like mobile language we have in that we use bcz,gn,gm so we want to replace it then we can 

############################################################
#autocorrect the sentence
from autocorrect import Speller
#declare the function speller defined for english
spell=Speller(lang='en')
spell("roww")   #'row'

#spanish
spell = Speller(lang='es')
# Correct a sample Spanish word
corrected_word = spell("espaol")
print(corrected_word)  # Output:espanol


############################################################
#autocorrect whole sentence
import nltk
nltk.download('punct')
from nltk import word_tokenize
sentence3="Natural language processing deals with art of extract"
#tokenize
sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join([spell(word)] for word in sentence3)
print(corrected_sentence)

############################################################











