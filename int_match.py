#!/usr/bin/env python

import numpy as np

def int_match(x,y)
    '''
    takes two lists of integers and returns the indexes of the list x into y
    '''
    index = np.argsort(x)
    sorted_x = x[index]
    ind = np.searchsorted(sorted_x,y)
    ind = index[ind]
    
    match=ind
    return match