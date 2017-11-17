# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 10:28:44 2017

@author: Dell
"""

import nltk
from collections import Counter
import csv


class Splitter(object):
    def __init__(self):
        self.nltk_splitter = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
        self.nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()

    def split(self, text):
        sentences = self.nltk_splitter.tokenize(text)
        tokenized_sentences = [self.nltk_tokenizer.tokenize(sent) for sent in sentences]
        return tokenized_sentences


class POSTagger(object):
    def __init__(self):
        pass
        
    def pos_tag(self, sentences):

        pos = [nltk.pos_tag(sentence) for sentence in sentences]
        pos = [[(word, word, [postag]) for (word, postag) in sentence] for sentence in pos]
        return pos
    
    
    
def value_of(sentiment):
    if sentiment == 'positive': return 1
    if sentiment == 'negative': return -1
    return 0

def sentiment_score(review):    
    return sum ([value_of(tag) for sentence in dict_tagged_sentences for token in sentence for tag in token[2]])

    
splitter = Splitter()
postagger = POSTagger()
cnter = []
pos_list = []
pos_list.append("good")
pos_list.append("great")
pos_list.append("excellent")
pos_list.append("nice")
pos_list.append("awesome")
pos_list.append("love")
text = []
with open("C:/Users/Dell/Downloads/1-restaurant-train.csv", "r", encoding='utf8') as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        text.append(line)
        cnter.append(0)
        #line=''.join(line)
        splitted_sentences = splitter.split(''.join(line))
        #print (splitted_sentences,'\n')
        pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
        #print (pos_tagged_sentences)
        for word in line:
            for token in word:
                print(word)
                if token in pos_list:
                    cnter[i]+=1
                if token in ('bad','worst','disappointed','expensive','avoid'):
                    cnter[i]-=1
        print(cnter[i])