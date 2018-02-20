# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:26:59 2018

@author: Jonas
"""

import indicoio
import numpy as np


def getValueAtIndex(dic, index):
    vals = list(dic.values())
    return vals[index]

def getKeyAtIndex(dic, index):
    keys = list(dic.keys())
    return keys[index]

def getArgMax(dic, rnd = 0):
    argMaxIndex = np.argmax(list(dic.values()))
    
    value = getValueAtIndex(dic, argMaxIndex)
    key = getKeyAtIndex(dic, argMaxIndex)
    
    if rnd:
        value = round(value, 2)
        
    return (key, value)


indicoio.config.api_key = 'a840148f0c38c41d3f70b43914656798'

text = "We're supposed to get up to 24 inches in the storm"

# single example
emotions = indicoio.emotion(text)

keywords = indicoio.keywords(text, version=2, relative=True)

print("Text: ", text)

print("Emotion: ", getArgMax(emotions, rnd=2))
print("Keyword: ", tuple((key, round(value, 2)) for key, value in list(keywords.items())))


