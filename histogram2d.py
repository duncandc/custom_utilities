#!/usr/bin/env python

#Duncan Campbell
#Yale University
#October 15, 2014
#Calculate a 2histogram and return indices of points in bins.

from __future__ import division
import numpy as np
import math
from scipy.spatial import cKDTree as KDT
import matplotlib.pyplot as plt

def main():
    
    x = np.random.random((10000,2))*0.5 #100 random 2D points between 0 and 1
    
    x[0,0]=0.1
    x[0,1]=0.9
    
    x[1,0]=0.9
    x[1,1]=0.1
    x[2,0]=0.91
    x[2,1]=0.11
    
    xbins = np.arange(0,1.1,0.1)
    ybins = np.arange(0,1.1,0.1)
    
    counts, inds = histogram2d(x[:,0],x[:,1],xbins, ybins)
    print counts
    print np.sum(counts,axis=0)
    
    plt.figure()
    for i in range(0,10):
        for j in range(0,10):
            selection = (inds[:,0]==i) & (inds[:,1]==j)
            plt.plot(x[:,0][selection],x[:,1][selection],'.')
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.show()

def histogram2d(x,y,xbins,ybins):

    inds = np.empty((len(x),2))
    inds[:,0] = np.digitize(x,xbins)-1
    inds[:,1] = np.digitize(y,ybins)-1
    
    counts = np.histogram2d(x,y,[xbins,ybins])[0]
    counts = np.rot90(counts)

    return counts, inds

if __name__ == '__main__':
    main()