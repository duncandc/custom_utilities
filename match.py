#!/usr/bin/env python

import numpy as np

def main():
    #example code calling match()
    x = np.random.permutation(np.arange(0,1000))
    x = np.random.permutation(x)
    y = np.random.permutation(x)
    match_into_y, matched_y = match(x,y)
    
    print np.all(x[match_into_y]==y[matched_y])

def match(x,y):
    '''
    takes two vectors of integers, x and y, where y must be a unique list 
    returns:
        indices of x which match into y
        matched indices of y
    '''
    
    #check to make sure the second list is unique
    if len(np.unique(y))!=len(y):
        "error: second array is not a unique array!"
        return None
        
    mask = np.where(np.in1d(y,x)==True)
    
    index_x = np.argsort(x)
    sorted_x = x[index_x]
    ind_x = np.searchsorted(sorted_x,y[mask])
    
    match1 = index_x[ind_x]
    
    return match1, mask
    
    
if __name__ == '__main__':
    main()