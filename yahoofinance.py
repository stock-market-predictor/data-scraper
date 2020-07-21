from bs4 import BeautifulSoup
import urllib
import re
import spacy
import  pandas as pd
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
import seaborn as sns
from  spacy.lang.en.stop_words import STOP_WORDS
from newspaper import Article
import en_core_web_sm

html_page = urllib.request.urlopen("https://finance.yahoo.com/news")
soup = BeautifulSoup(html_page)
returnlist = []
for link in soup.findAll('a'):
    if link.get('href')[0:5] == '/news':

        returnlist.append('https://finance.yahoo.com' + link.get('href'))

url = returnlist[0]
article = Article(url)
article.download()
article.parse()
article.nlp()
nlp = en_core_web_sm.load()
stopwords = list(STOP_WORDS)
doc = nlp(article.text)
