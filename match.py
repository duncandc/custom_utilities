#!/usr/bin/env python

import numpy as np

def main():
    '''
    example code calling match()
    '''
    
    x = np.random.permutation(np.arange(0,1000))
    x = np.random.permutation(x)
    y = np.random.permutation(x)
    match_into_y, matched_y = match(x,y)
    
    print np.all(x[match_into_y]==y[matched_y])

def match(x,y):
    '''
    determines the indices of matches in list one into list two
    
    paramters
    x: list to be matched
    y: unique list to matched against
    
    retruns:
    matches: indices in list one that return matches into list 2
    matched: indices of list 2
    '''
    
    #check to make sure the second list is unique
    if len(np.unique(y))!=len(y):
        "error: second array is not a unique array! returning no matches."
        return None
    
    mask = np.where(np.in1d(x,y)==True)[0]
    
    index_y = np.argsort(y)
    sorted_y = y[index_y]
    ind_y = np.searchsorted(sorted_y,x[mask])
    ind_y = index_y[ind_y]
    
    matched = ind_y
    matches = mask
    
    return matches, matched
    
    
if __name__ == '__main__':
    main()