#!/usr/bin/env python

from ..spherematch import spherematch
from ..sample_ra_dec_box import sample_ra_dec_box
import numpy as np

def test_self_match():
    import random
    ra_min, ra_max = (209.0,220.0)
    dec_min, dec_max = (51.0,58.0)
    N=1000
    
    sample1 = sample_ra_dec_box(ra_min, ra_max, dec_min, dec_max, N)
    sample2 = sample1[:]
    random.shuffle(sample2)
    
    ra1,dec1 = zip(*sample1)
    ra2,dec2 = zip(*sample2)
    
    idxs1, idxs2, ds = spherematch(ra1,dec1,ra2,dec2,tol=0.01,nnearest=1,threads=1)
    
    assert np.sum(ds)==0, "non-zero angular seperation to self"
    
    sample1 = np.array(sample1)
    sample2 = np.array(sample2)
    
    assert np.all(sample1[idxs1]==sample2[idxs2]), "index into 2nd array doesnt return self"
    
def test_close_match():
    import random
    ra_min, ra_max = (209.0,220.0)
    dec_min, dec_max = (51.0,58.0)
    N=1000
    
    sample1 = sample_ra_dec_box(ra_min, ra_max, dec_min, dec_max, N)
    sample2 = sample1[:]
    random.shuffle(sample2)
    
    ra1,dec1 = zip(*sample1)
    ra2,dec2 = zip(*sample2)
    
    ra2 = np.array(ra2) + np.random.randn(N)*0.001
    dec2 = np.array(dec2) + np.random.randn(N)*0.001/2.0
    
    idxs1, idxs2, ds = spherematch(ra1,dec1,ra2,dec2,tol=0.01,nnearest=1,threads=1)
    
    
    
    