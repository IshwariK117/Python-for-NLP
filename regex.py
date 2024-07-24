
#18 june 2024
#########################################################33
#regx
import re
chat1="Hello, I am having issue with my order #4123567"

pattern='order[^d]*(\d*)'
matches=re.findall(pattern,chat1)
matches

chat2="I have a problem with my order number 21267112"
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat2)
matches
chat3="I have 21267112 a problem, with my order number "
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat3)
matches


####################################################
import re
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]*(\d*)',chat1)

#######################################
chat1=' you ask lot of questions 12345678912, abc@xyz.com'
chat2='here it is:(123)-567-8912,abc@xyz.com'
chat3='yes,phone:12345678912 email:abc@xyz.com'
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*', chat1)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*', chat2)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*', chat3)

#######################################################
#patterns for all types of numbers
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat1)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat2)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat3)

#########################################################

text='''Born Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship
South Africa
Canada
United States
Education University of Pennsylvania (BA, BS)
Title
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses
Justine Wilson

(m. 2000; div. 2008)
Talulah Riley

(m. 2010; div. 2012)

(m. 2013; div. 2016)'''

get_pattern_match(r'age (\d+)',text)
get_pattern_match(r'Born(.*)\n', text).strip()
get_pattern_match(r'Born.*\n(.*)\(age', text).strip()
get_pattern_match(r'\(age.*\n(.*)', text)

#-------------------------------------------------------------------
#19 June 2024
def extract_personal_information(text):
   age=get_pattern_match('age (\d+)',text)
   full_name=get_pattern_match('Born(.*)\n', text)
   birth_date=get_pattern_match('Born.*\n(.*)\(age', text)
   birth_place=get_pattern_match('\(age.*\n(.*)', text)
   return{
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()}
text='''Ambani in 2007
Born Mukesh Dhirubhai Ambani
19 April 1957 (age 67)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality Indian
Alma mater
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s) Chairman and MD, Reliance Industries
Spouse Nita Ambani (m. 1985)[3]
Children 3
Parents
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives Anil Ambani (brother)
Tina Ambani (sister-in-law)'''
extract_personal_information(text)
#imports

