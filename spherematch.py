"""
Match two sets of on-sky coordinates to each other.
I.e., find nearest neighbor of one that's in the other.
 
Similar in purpose to IDL's spherematch, but totally different implementation.
 
Requires numpy and scipy.
"""

from __future__ import division
import numpy as np
import math
try:
  from scipy.spatial import cKDTree as KDT
except ImportError:
  from scipy.spatial import KDTree as KDT

import time
 
 
 
def spherematch(ra1, dec1, ra2, dec2, tol=None, nnearest=1, threads=1):
    """
    Finds matches in one catalog to another.
 
    Parameters
    ra1 : array-like
        Right Ascension in degrees of the first catalog
    dec1 : array-like
        Declination in degrees of the first catalog (shape of array must match `ra1`)
    ra2 : array-like
        Right Ascension in degrees of the second catalog
    dec2 : array-like
        Declination in degrees of the second catalog (shape of array must match `ra2`)
    tol : float or None, optional
        How close (in degrees) a match has to be to count as a match.  If None,
        all nearest neighbors for the first catalog will be returned.
    nnearest : int, optional
        The nth neighbor to find.  E.g., 1 for the nearest nearby, 2 for the
        second nearest neighbor, etc.  Particularly useful if you want to get
        the nearest *non-self* neighbor of a catalog.  To do this, use:
        ``spherematch(ra, dec, ra, dec, nnearest=2)``
 
    Returns
    -------
    idx1 : int array
        Indecies into the first catalog of the matches. Will never be
        larger than `ra1`/`dec1`.
    idx2 : int array
        Indecies into the second catalog of the matches. Will never be
        larger than `ra1`/`dec1`.
    ds : float array
        Distance (in degrees) between the matches
    """
 

    ra1 = np.array(ra1, copy=False)
    dec1 = np.array(dec1, copy=False)
    ra2 = np.array(ra2, copy=False)
    dec2 = np.array(dec2, copy=False)

 
    if ra1.shape != dec1.shape:
        raise ValueError('ra1 and dec1 do not match!')
    if ra2.shape != dec2.shape:
        raise ValueError('ra2 and dec2 do not match!')  

    x1, y1, z1 = _spherical_to_cartesian_fast(ra1.ravel(), dec1.ravel(), threads) 

    # this is equivalent to, but faster than just doing np.array([x1, y1, z1])
    coords1 = np.empty((x1.size, 3))
    coords1[:, 0] = x1
    coords1[:, 1] = y1
    coords1[:, 2] = z1   

    x2, y2, z2 = _spherical_to_cartesian_fast(ra2.ravel(), dec2.ravel(), threads)

    # this is equivalent to, but faster than just doing np.array([x1, y1, z1])
    coords2 = np.empty((x2.size, 3))
    coords2[:, 0] = x2
    coords2[:, 1] = y2
    coords2[:, 2] = z2
 
    kdt = KDT(coords2)
    if nnearest == 1:
        idxs2 = kdt.query(coords1)[1]
    elif nnearest == 0 and (tol is not None):  #if you want all matches
        p1x, p1y, p1z = _spherical_to_cartesian_fast(90, 0, threads)
        p2x, p2y, p2z = _spherical_to_cartesian_fast(90, tol, threads)
        p1x = float(p1x)
        p2x = float(p2x)
        p1y = float(p1y)
        p2y = float(p2y)
        p1z = float(p1z)
        p2z = float(p2z)
        r = np.sqrt((p2x-p1x)**2+(p2y-p1y)**2+(p2z-p1z)**2) #cartesian tol
        idxs2 = kdt.query_ball_point(coords1, r)[0]
    elif nnearest > 1:
        idxs2 = kdt.query(coords1, nnearest)[1][:, -1]
    else:
        raise ValueError('invalid nnearest ' + str(nnearest))
 
    ds = _great_circle_distance_fast(ra1, dec1, ra2[idxs2], dec2[idxs2], threads) 


    idxs1 = np.arange(ra1.size)
 
    if (tol is not None) and nnearest != 0:
        msk = ds < tol
        idxs1 = idxs1[msk]
        idxs2 = idxs2[msk]
        ds = ds[msk]

 
    return idxs1, idxs2, ds
 
 
def _spherical_to_cartesian(ra, dec):
    """
    (Private internal function)
    Inputs in degrees.  Outputs x,y,z
    """
    rar = np.radians(ra)
    decr = np.radians(dec)

    x = np.cos(rar) * np.cos(decr)
    y = np.sin(rar) * np.cos(decr)
    z = np.sin(decr)
 
    return x, y, z

def _spherical_to_cartesian_fast(ra, dec, threads):
    """
    (Private internal function)
    Inputs in degrees.  Outputs x,y,z
    """
    import numexpr as ne

    #nthreads = ne.detect_number_of_cores()
    nthreads = threads
    ne.set_num_threads(nthreads)

    pi = math.pi
    rar = ne.evaluate('ra*pi/180.0')
    decr = ne.evaluate('dec*pi/180.0')

    hold1=ne.evaluate('cos(decr)') 

    x = ne.evaluate('cos(rar) * hold1')
    y = ne.evaluate('sin(rar) * hold1')
    z = ne.evaluate('sin(decr)')
 
    return x, y, z
 
 
def _great_circle_distance(ra1, dec1, ra2, dec2):
    """
    (Private internal function)
    Returns great circle distance.  Inputs in degrees.
 
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


def _great_circle_distance_fast(ra1, dec1, ra2, dec2, threads):
    """
    (Private internal function)
    Returns great circle distance.  Inputs in degrees.
 
    Uses vicenty distance formula - a bit slower than others, but
    numerically stable.

    A faster version than the function above.
    """

    import numexpr as ne
 
    # terminology from the Vicenty formula - lambda and phi and
    # "standpoint" and "forepoint"
    lambs = np.radians(ra1)
    phis = np.radians(dec1)
    lambf = np.radians(ra2)
    phif = np.radians(dec2)
 
    dlamb = lambf - lambs

    #using numexpr
    #nthreads = ne.detect_number_of_cores()
    nthreads = threads
    ne.set_num_threads(nthreads)

    hold1=ne.evaluate('sin(phif)') #calculate these once instead of a few times!
    hold2=ne.evaluate('sin(phis)')
    hold3=ne.evaluate('cos(phif)')
    hold4=ne.evaluate('cos(dlamb)')
    hold5=ne.evaluate('cos(phis)')
    numera = ne.evaluate( 'hold3 * sin(dlamb)')
    numerb = ne.evaluate('hold5 * hold1 - hold2 * hold3 * hold4')
    numer = ne.evaluate('sqrt(numera**2 + numerb**2)')
    denom = ne.evaluate('hold2 * hold1 + hold5 * hold3 * hold4')
    pi=math.pi

    return ne.evaluate('(arctan2(numer, denom))*180.0/pi')
