# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:55:42 2020

@author: Python
"""

from textblob import TextBlob
 
text = TextBlob("It was a mediocre movie. I somewhat liked it very much.")
 
print (text.sentiment)
print ('polarity: {}'.format(text.sentiment.polarity))
print ('subjectivity: {}'.format(text.sentiment.subjectivity))

 
text = TextBlob("I liked the acting of the lead actor but I didn't like the movie overall.")
print (text.sentiment)


 
text = TextBlob("I liked the acting of the lead actor and I like the movie overall.")
print (text.sentiment)


from textblob import TextBlob
 
text = TextBlob("It was a lousy movie. I thought it was fine.")
 
print (text.sentiment)
print ('polarity: {}'.format(text.sentiment.polarity))
print ('subjectivity: {}'.format(text.sentiment.subjectivity))

 
text = TextBlob("I liked the acting of the lead actor but I didn't like the movie overall.")
print (text.sentiment)


 
text = TextBlob("I liked the acting of the lead actor and I liked the movie overall.")
print (text.sentiment)
