#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    swap=sentence.swapcase()
    newlist=list(swap.split())
    string=''
    for i in range(len(newlist)-1,-1,-1):
        string += newlist[i]+" "
    return string
    
    
if __name__ == '__main__':