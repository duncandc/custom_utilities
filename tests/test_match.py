#!/usr/bin/env python

from ..match import match
import numpy as np

def test_match_one_to_one():
    x = np.random.permutation(np.arange(0,1000))
    x = np.random.permutation(x)
    y = np.random.permutation(x)
    match_into_y, matched = match(x,y)
    assert np.all(x[match_into_y]==y[matched]), "matched x does not equal y matched"
    
def test_match_nonunique_error():
    x = np.random.permutation(np.arange(0,1000))
    x = np.random.permutation(x)
    y = np.random.permutation(x)
    y[:100]=y[-100:]
    result = match(x,y)
    assert result is None, "no non-unique second array error thrown"
    
def test_match_sparse_matched():
    x = np.random.permutation(np.arange(0,1000))
    x = np.random.permutation(x)
    y = np.random.permutation(np.arange(900,1900))
    y = np.random.permutation(y)
    match_into_y, matched = match(x,y)
    assert np.all(x[match_into_y]==y[matched]), "matched x does not equal y matched"
    
def test_match_many_to_one():
    x = np.random.random_integers(0,1000,1000)
    y = np.arange(0,1000)
    y = np.random.permutation(y)
    match_into_y, matched = match(x,y)
    assert len(np.unique(match_into_y))==len(match_into_y), "element in x matched\
                                                             multiple times"
    assert np.all(x[match_into_y]==y[matched]), "matched x does not equal y matched"