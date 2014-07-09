#!/usr/bin/env python

from ..sample_spherical_cap import sample_spherical_cap
import numpy as np

def test_number():
    ra = 215.0
    dec = 55.0
    da = 4.0
    N=1000
    
    sample = sample_spherical_cap(ra,dec,da,N)
    ra,dec = zip(*sample)
    
    assert len(sample)>= N, 'fewer points sampled than required.'
    assert len(sample)<= N, 'more points sampled than required.'