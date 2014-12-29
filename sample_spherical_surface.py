#!/usr/bin/env python

# Duncan Campbell
# Written: December, 29 2014
# Yale University
# Sample the surface of a sphere with N random points. 
# Return the coordinates ra,dec of the points.

from __future__ import division
import numpy as np
import math

def main():
    '''
    Example script calling sample_spherical_cap() function to give random ra,dec points in
    a specified region.
    '''
    
    import matplotlib.pyplot as plt
    N=10000
    
    sample = sample_spherical_surface(N)
    
    ra,dec = zip(*sample)
    ra=np.array(ra)
    dec=np.array(dec)
    
    plt.plot(ra,np.sin(dec*2.0*math.pi/360.0)*90.0,'.',color='blue')
    plt.xlabel('RA')
    plt.ylabel('DEC')
    plt.ylim([-90,90])
    plt.xlim([0,360])
    plt.show()
    

def sample_spherical_surface(N_points):
    '''
    Randomly sample the sky.
    
    Parameters 
    ----------
    N_points: int
        number of points to sample on cap.
    
    Returns 
    ----------
    coords: list 
        (ra,dec) coordinate pairs in spherical cap region.
    '''

    from numpy import random
    from numpy import sin, cos
    from math import pi

    ran1 = random.rand(N_points) #oversample, to account for box sample  
    ran2 = random.rand(N_points) #oversample, to account for box sample

    ran1 = ran1 * 2.0 * pi #convert to radians
    ran2 = np.arccos(2.0 * ran2 - 1.0) - 0.5*pi #convert to radians

    ran1 = ran1 * 360.0 / (2.0 * pi) #convert to degrees 
    ran2 = ran2 * 360.0 / (2.0 * pi) #convert to degrees

    ran_ra = ran1
    ran_dec = ran2

    coords = zip(ran_ra,ran_dec)

    return coords


if __name__ == '__main__':
    main()