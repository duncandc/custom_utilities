#!/usr/bin/env python

from ..inside import inside
import numpy as np

def test_inside_square():
    #define square
    square = [(-1,-1),(-1,1),(1,1),(1,-1)]
    
    #define test points
    p1 = (0,0) #inside
    p2 = (-1,2) #outside
    
    result = inside(p1[0],p1[1],square)
    
    assert result, "failed to locate point inside polygon"
    
    result = inside(p2[0],p2[1],square)
    
    assert not result, "failed to locate point outside polygon"