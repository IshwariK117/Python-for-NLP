
'''
pip install PyPDF2

'''
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader
reader = PdfReader('C:\\1-Python\\kopargaon-part-1.pdf')
print(len(reader.pages))

page=reader.page[1]
text=page.extract_text()
print(text)

from PyPDF import PdfFileReader
from PyPDF2 import PdfReader

reader=PdfReader('C:\1-Python\matrix_basics.pdf')
print(len(reader.pages))

page=reader.pages[1]
text=page.extract_text()
print(text)


#********************************************************

import re
sentence5="sharad twitted ,witnessing 68th republic day india from Rajpath,\new Delhi,Mesmorizing performance by Indian Army!"
re.sub(r'([^\s\w]|_)+',' ',sentence5).split()
#-------------------------------------------
#extracting n-grams using custom defined functions

import re 
def n_gram_extractor(input_str,n):
    tokens=re.sub(r'([^\s\w]|_)+',' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
        
n_gram_extractor("The cute little boy is playing with kitten",2)
n_gram_extractor("The cute little boy is playing with kitten",3)

#---------------------------------------------
from nltk import ngrams       #ngrams like diagrams,trigrams
#extrcation of n-grams with nltk
list(ngrams("the cute little boy is playing with kitten ".split(),2))
list(ngrams("the cute little boy is playing with kitten ".split(),3))

#--------------------------------------------
'''
pip installl textblob
'''
from textblob import TextBlob
blob=TextBlob("The cute little boy is playing with kiten")
blob.ngrams(n=2)
blob.ngrams(n=3)
  
#----------------------------------------------
'''
pip install Keras
'''
sentence5="sharad twitted ,witnessing 68th republic day india from Rajpath,\new Delhi,Mesmorizing performance by Indian Army!"
sentence5
from keras.preprocessing.text import text_to_word_sentence
text_to_word_sentence(sentence5)

#-----------------------------------------------
#Tokenizer using textBlob
from textblob import TextBlob
blob=TextBlob(sentence5)
blob.words

#------------------------------------------------
#tweet tokenizer
from nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer()
tweet_tokenizer.tokenize(sentence5)



#------------------------------------------------
from nltk.tokenize import MWETokenizer
'''
multi word tokenizers are essential for tasks where 
the meaning of  text is heavily depends on the
interpretation of phases as wholes ratherv than 
as i=sums of individual words,for instance,as 
sentiment analysis ,recognizing 'not good' as a 
single negative sentiment unit rather than as 'not' 
and 'good' separtely can significantly affect the 
outcome

'''
sentence5
mwe_tokenizer=MWETokenizer([('republic','day')])
mwe_tokenizer.tokenize(sentence5.split())
mwe_tokenizer.tokenize(sentence5.replace('!',' ').split())








