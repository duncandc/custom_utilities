#Duncan Campbell
#August 22, 2014
#Yale University
#Calculate the number of pairs with separations less than r.

cimport cython
import numpy as np
from libc.math cimport sqrt, floor, fabs

@cython.boundscheck(False)
@cython.wraparound(False)
def npairs(double[:, ::1] data1, double[:, ::1] data2, double[:] rbins):
    """
    Calculate the number of pairs with separations less than or equal to rbins[i].
    
    Parameters
    ----------
        data1: array_like
            N by k numpy array of k-dimensional positions. Should be between zero and 
            period
            
        data2: array_like
            N by k numpy array of k-dimensional positions. Should be between zero and 
            period
            
        rbins : array_like
            numpy array of boundaries defining the bins in which pairs are counted. 
            len(rbins) = Nrbins + 1.
            
        period: array_like, optional
            length k array defining axis-aligned periodic boundary conditions. If only 
            one number, Lbox, is specified, period is assumed to be np.array([Lbox]*k).
            If none, PBCs are set to infinity.
            
    Returns
    -------
    N_pairs : array of length len(rbins)
        number counts of pairs
     
    """
    
    #work with arrays!
    data1 = np.asarray(data1)
    if data1.ndim ==1: data1 = np.array([data1])
    data2 = np.asarray(data2)
    if data2.ndim ==1: data2 = np.array([data2])
    rbins = np.asarray(rbins)
    if rbins.size ==1: rbins = np.array([rbins])
    
    #Check to make sure both data sets have the same dimension. Otherwise, throw an error!
    if np.shape(data1)[-1]!=np.shape(data2)[-1]:
        raise ValueError("data1 and data2 inputs do not have the same dimension.")
        return None
        
    #Process period entry and check for consistency.
    if period is None:
            period = np.array([np.inf]*np.shape(data1)[-1])
    else:
        period = np.asarray(period).astype("float64")
        if np.shape(period) == ():
            period = np.array([period]*np.shape(data1)[-1])
        elif np.shape(period)[0] != np.shape(data1)[-1]:
            raise ValueError("period should have len == dimension of points")
            return None

    
    cdef int M = data1.shape[0]
    cdef int N = data2.shape[1]
    cdef int nbins = rbins.shape[0]
    cdef double tmp, d
    cdef long[:] counts = np.zeros((nbins,), dtype=np.int)
    cdef int i,j,k
    
    for i in range(M):
        for j in range(M):
            d = 0.0
            for k in range(N):
                tmp = data1[i, k] - data2[j, k]
                d += tmp * tmp
            d = sqrt(d)
            k = nbins-1
            while d<=rbins[k]:
                counts[k] += 1
                k=k-1
                if k<0: break
                
    return np.asarray(counts)
    
    
    