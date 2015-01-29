#!/usr/bin/env python
# cython: profile=False

#Duncan Campbell
#August 22, 2014
#Yale University
#return a list of matches between two arrays, both can be non-unique

from __future__ import print_function, division
cimport cython
cimport numpy as np
import numpy as np

__all__=['match2']

@cython.boundscheck(False)
@cython.wraparound(False)
def match2(x, y):
    """
    for each x, return the matches in y
    
    Parameters
    ==========
    x, array_like
        integer array
    
    y, array_like
        integer array
    
    Return
    ======
    inds, 
    list of length len(x).  Each element in the list, corresponding to an entry in x, is a
    list of indices in y which match.
    """
    
    cdef long [:] cx = x
    cdef long [:] cy = y
    cdef int i,j
    
    Nx = len(x)
    Ny = len(y)
    
    #initialize list to store result in
    result = []
    for i in range(Nx):
        result.append([])
    
    #loop through each object in x and check for a match in y
    for i in range(Nx):
        xx = cx[i]
        for j in range(Ny):
            if xx==cy[j]: result[i].append(j)
    
    return result
    

