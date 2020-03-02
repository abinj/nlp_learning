# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:48:20 2020

@author: Python
"""
#import library
import nltk
nltk.download('stopwords')

#retrieve data source and view source
import urllib.request
response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()
print(html)

#Using scraper tool "BeautifuLSoup" to scrape html and xml files 
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html.parser')
text = soup.get_text(strip = True)
print(text)
#convert text into tokens
tokens = [t for t in text.split()]
print(tokens)
#Remove stopwords and visualize outcome
from nltk.corpus import stopwords
sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)


