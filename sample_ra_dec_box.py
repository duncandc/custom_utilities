#!/usr/bin/env python

# Duncan Campbell
# Written: July 7, 2014
# Yale University
# Sample a spherical box region with N random points. 
# Return the coordinates of the points.

from __future__ import division
import numpy as np

def main():
    #example code calling sample_ra_dec_box() to give random ra,dec points in a specified 
    #region
    import matplotlib.pyplot as plt
    #define region, e.g. roughly the W3 CFHTLS field
    ra_min, ra_max = (209.0,220.0)
    dec_min, dec_max = (51.0,58.0)
    N=1000
    
    sample = sample_ra_dec_box(ra_min, ra_max, dec_min, dec_max, N)
    
    ra,dec = zip(*sample)
    
    plt.plot([ra_min,ra_min,ra_max,ra_max,ra_min],\
             [dec_min,dec_max,dec_max,dec_min,dec_min],color='orange')
    plt.plot(ra,dec,'.',color='blue')
    plt.xlim([205,225])
    plt.ylim([50,60])
    plt.show()
    

def sample_ra_dec_box(ra_min, ra_max, dec_min, dec_max, N_points):
    '''
    Randomly sample a spherical region bounded by ra_min, ra_max, dec_min, dec_max
    
    Parameters 
    ----------
    ra_min: float
        minimum angular coordinate in degrees
        
    dec_min: float
        minimum angular coordinate in degrees
        
    ra_max: float
        minimum angular coordinate in degrees
        
    dec_max: float
        minimum angular coordinate in degrees
        
    N_points: int
        number of points to return in region
    
    Returns 
    ----------
    coords: list
        N_pints (ra,dec) coordinate pairs in region
    '''

    from numpy import random
    from numpy import sin, cos
    from math import pi
    
    ra_max = np.radians(ra_max)
    ra_min = np.radians(ra_min)
    dec_max = np.radians(dec_max)
    dec_min = np.radians(dec_min)

    ra_max = ra_max / (2.0* pi) #map onto (0,1)
    ra_min = ra_min / (2.0* pi) #map onto (0,1)
    dec_max = (cos(dec_max + 0.5*pi) + 1.0) / 2.0 #map onto (0,1)
    dec_min = (cos(dec_min + 0.5*pi) + 1.0) / 2.0 #map onto (0,1)

    ran1 = random.rand(N_points)
    ran2 = random.rand(N_points)

    ran1 = ran1 * (ra_max-ra_min) + ra_min #scale so it falls in field
    ran1 = ran1 * 2.0 * pi #convert to radians

    ran2 = ran2 * (dec_max - dec_min) + dec_min #scale so it falls in field
    ran2 = np.arccos(2.0 * ran2 - 1.0) - 0.5*pi #convert to radians

    ran_ra = ran1 * 360.0 / (2.0 * pi) #convert to degrees 
    ran_dec = ran2 * 360.0 / (2.0 * pi) #convert to degrees

    coords = zip(ran_ra,ran_dec)

    return coords
    
if __name__ == '__main__':
    main()