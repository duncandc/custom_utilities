#!/usr/bin/env python

from ..sample_ra_dec_box import sample_ra_dec_box
import numpy as np

def test_match_one_to_one():
    #define region, e.g. roughly the W3 CFHTLS field
    ra_min, ra_max = (209.0,220.0)
    dec_min, dec_max = (51.0,58.0)
    N=1000
    
    sample = sample_ra_dec_box(ra_min, ra_max, dec_min, dec_max, N)
    ra,dec = zip(*sample)
    
    assert len(sample)== N, 'fewer points sampled than required.'
    assert min(ra)>=ra_min, 'ra points out of region'
    assert min(dec)>=dec_min, 'dec points out of region'
    assert max(ra)<=ra_max, 'ra points out of region'
    assert max(dec)<=dec_max, 'dec pionts out of region'