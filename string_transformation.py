#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    words = sentence.split()
    res = []
    
    for word in words:
        transformed_word = word[0]  # First character remains the same
        for j in range(1, len(word)):
            if word[j-1].lower() < word[j].lower():
                transformed_word += word[j].upper()
            elif word[j-1].lower() > word[j].lower():
                transformed_word += word[j].lower()
            else:
                transformed_word += word[j]
        res.append(transformed_word)
    
    return " ".join(res)
       
if __name__ == '__main__':