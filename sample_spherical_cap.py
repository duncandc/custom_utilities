#!/usr/bin/env python

# Duncan Campbell
# Written: August 2, 2013
# Yale University
# Sample a spherical cap region of a sphere with N random points. 
# Return the coordinates of the points.

from __future__ import division
import numpy as np

def main():
    #example code calling sample_spherical_cap() to give random ra,dec points in a specified 
    #region
    import matplotlib.pyplot as plt
    #define region, e.g. roughly the W3 CFHTLS field
    ra = 215.0
    dec = 55.0
    da = 4.0
    N=1000
    
    sample = sample_spherical_cap(ra,dec,da,N)
    print sample
    ra,dec = zip(*sample)
    
    plt.plot(ra,dec,'.',color='blue')
    #plt.xlim([205,225])
    #plt.ylim([50,60])
    plt.show()
    

def sample_spherical_cap(ra, dec, da, N_points):
    '''
    randomly sample a spherical cap
    
    parameters
    ra: angular coordinate to center on
    dec: angular coordinate to center on
    da: angular radius of spherical cap
    N_points: number of points to sample cap
    
    returns
    coords: list of N_pints (ra,dec) coordinate pairs in spherical cap region
    '''

    from numpy import random
    from numpy import sin, cos
    from math import pi

    ra_max = (ra + da / np.cos((dec * 2.0 * pi) / 360.0)) * (2.0 * pi) / 360.0 
    ra_min = (ra - da / np.cos((dec * 2.0 * pi) / 360.0)) * (2.0 * pi) / 360.0
    dec_max = (dec + da) * (2.0 * pi) / 360.0
    dec_min = (dec - da) * (2.0 * pi) / 360.0

    ra_max = ra_max / (2.0* pi) #map onto (0,1)
    ra_min = ra_min / (2.0* pi) #map onto (0,1)
    dec_max = (cos(dec_max + 0.5 * pi) + 1.0) / 2.0 #map onto (0,1)
    dec_min = (cos(dec_min + 0.5 * pi) + 1.0) / 2.0 #map onto (0,1)
    print dec_min, dec_max
    print ra_min, ra_max

    ran1 = random.rand(N_points * 3.0) #oversample, to account for box sample  
    ran2 = random.rand(N_points * 3.0) #oversample, to account for box sample

    ran1 = ran1 * (ra_max-ra_min) + ra_min #scale so it falls in field
    ran1 = ran1 * 2.0 * pi #convert to radians

    ran2 = ran2 * (dec_max - dec_min) + dec_min #scale so it falls in field
    ran2 = np.arccos(2.0 * ran2 - 1.0) - 0.5*pi #convert to radians

    ran1 = ran1 * 360.0 / (2.0 * pi) #convert to degrees 
    ran2 = ran2 * 360.0 / (2.0 * pi) #convert to degrees
    
    r = _sphdist(ra, dec, ran1, ran2) #calculate angular distance from center
    inside_cap = (np.where(r < da))[0][0:N_points] #only use points with r<da
    ran_ra = ran1[inside_cap]
    ran_dec = ran2[inside_cap]

    coords = zip(ran_ra,ran_dec)

    return coords

def _sphdist(ra1, dec1, ra2, dec2):
    """
    (Private internal function)
    Returns great circle distance.  Inputs in degrees.

    ra1, dec1 must of length 1, returns the distances in deg
 
    Uses vicenty distance formula - a bit slower than others, but
    numerically stable.
    """
    
    from numpy import radians, degrees, sin, cos, arctan2, hypot 

    # terminology from the Vicenty formula - lambda and phi and
    # "standpoint" and "forepoint"
    lambs = radians(ra1)
    phis = radians(dec1)
    lambf = radians(ra2)
    phif = radians(dec2)
 
    dlamb = lambf - lambs
 
    numera = cos(phif) * sin(dlamb)
    numerb = cos(phis) * sin(phif) - sin(phis) * cos(phif) * cos(dlamb)
    numer = hypot(numera, numerb)
    denom = sin(phis) * sin(phif) + cos(phis) * cos(phif) * cos(dlamb)

    return degrees(np.arctan2(numer, denom))


if __name__ == '__main__':
    main()