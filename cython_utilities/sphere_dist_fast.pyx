import numpy as np
cimport numpy as np
cimport cython

cdef extern from "math.h":
    double acos(double)
    double fabs(double)
    long floor(double)

from libc.stdlib cimport malloc, free

@cython.boundscheck(False)
@cython.wraparound(False)
def sphere_dist(np.ndarray[np.float64_t, ndim=2] x1,\
                np.ndarray[np.float64_t, ndim=2] x2):
    """
    Return anglular seperation, da, between points, x1, and points, x2 in acos(da).
    x1 must be an array of 3D vectors (shorter list)
    x2 must be an array of 3D vectors (longer list)
    """
    
    cdef unsigned int N2
    N2 = len(x2)
    cdef unsigned int N1
    N1 = len(x1)

    cdef np.ndarray[np.float64_t, ndim=2] da 
    da = np.empty((N1,N2), dtype=np.float64)

    cdef double dot    

    cdef unsigned int i
    cdef unsigned int j
    for i in range(N1):
        for j in range(N2):
            #find the angular seperation
            dot = (x1[i,0]*x2[j,0]) + (x1[i,1]*x2[j,1]) + (x1[i,2]*x2[j,2])
            #da[i,j] = acos(dot) #use this to get results in radians
            da[i,j] = dot
        
    return da

@cython.boundscheck(False)
@cython.wraparound(False)
def sphere_dist_binned(np.ndarray[np.float64_t, ndim=2] x1,\
                np.ndarray[np.float64_t, ndim=2] x2,\
                np.ndarray[np.float64_t, ndim=1] bins):
    """
    Return anglular seperation histogram for bins=bins in rad
    between a point, x1, and points, x2 in radians.
    x1 must be an array of 3D vectors (shorter list)
    x2 must be an array of 3D vectors (longer list)
    bins must be monotonically increasing, equal sized,
    and cover the full range of outcomes
    """
    print 'here'

    cdef unsigned int N1 #number of vectors in x1
    N1 = len(x1)
    cdef unsigned int N2 #number of vectors in x2
    N2 = len(x2)

    cdef unsigned int N_bin #number of bins
    N_bins = len(bins)-1
    cdef double bin_size #size of bins, must be equal sized
    bin_size = fabs(bins[1]-bins[0])
    cdef double inv_bin_size #save some calculation time below
    inv_bin_size = 1.0/bin_size
    cdef double min_bin #minimum lower bin bound
    min_bin = min(bins)
    cdef int bin_ind_dec #bin index decrement from 0
    bin_ind_dec = int(min_bin*inv_bin_size) 

    cdef np.ndarray[np.int_t, ndim=1] count #histogram
    count = np.zeros((N_bins,), dtype=np.int) #intialize to zero

    cdef double da #angular seperation
    cdef double dot #dot product 
    cdef unsigned int i #counter
    cdef unsigned int j #counter
    for i in range(N1):
        for j in range(N2):
            #find the angular seperation
            dot = (x1[i,0]*x2[j,0]) + (x1[i,1]*x2[j,1]) + (x1[i,2]*x2[j,2])
            da = acos(dot) #use this to get results in radians
            #da = dot #use this to get results in acos(da)
            #create histogram
            k = floor(da*inv_bin_size)-bin_ind_dec #zero index histogram
            count[k] += 1  
    print count     
    return count
