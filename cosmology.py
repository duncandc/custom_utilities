#Duncan Campbell
#June 2, 2015
#Yale University

""" 
cosmological distance calculations
"""

from __future__ import division, print_function

__all__=['hubble_distance','comoving_distance','transverse_comoving_distance',\
         'angular_diameter_distance','luminosity_distance','comoving_volume']

import numpy as np
import astropy.cosmology
import scipy.integrate as integrate

c = 299792.458 #speed of light (km/s)

def hubble_distance(H0):
    """
    Calculate the Hubble distance
    
    parameters
    ----------
    H0: float
        Hubble constant in km/s/Mpc
    
    returns
    -------
    DH: float
        Hubble distance in Mpc
    """
    return c/H0


def comoving_distance(z,cosmo=None):
    """
    Calculate the line of sight comoving distance
    
    parameters
    ----------
    z: float
        redshift
    
    cosmo: astropy.cosmology object, optional
        cosmology object specifying cosmology.  If None,  FlatLambdaCDM(H0=70,Om0=0.3)
    
    returns
    -------
    DC: float
        Comoving line of sight distance in Mpc
    """
    
    if cosmo==None:
        cosmo = astropy.cosmology.FlatLambdaCDM(H0=70, Om0=0.3)
    
    f = lambda zz: 1.0/_Ez(zz, cosmo.Om0, cosmo.Ok0, cosmo.Ode0)
    DC = integrate.quadrature(f,0.0,z)[0]
    
    return hubble_distance(cosmo.H0.value)*DC


def transverse_comoving_distance(z,cosmo=None):
    """
    Calculate the transverse comoving distance
    
    parameters
    ----------
    z: float
        redshift
    
    cosmo: astropy.cosmology object, optional
        cosmology object specifying cosmology.  If None,  FlatLambdaCDM(H0=70,Om0=0.3)
    
    returns
    -------
    DM: float
        Comoving transverse distance in Mpc
    """
    
    if cosmo==None:
        cosmo = astropy.cosmology.FlatLambdaCDM(H0=70, Om0=0.3)
    
    if cosmo.Ok0==0.0:
        return comoving_distance(z,cosmo)
    elif cosmo.Ok0>0:
        DC = comoving_distance(z,cosmo)
        DH = hubble_distance(cosmo.H0.value)
        return DH*1.0/np.sqrt(cosmo.Ok0)*np.sinh(np.sqrt(cosmo.Ok0)*DC/DH)
    elif cosmo.Ok0<0:
        DC = comoving_distance(z,cosmo)
        DH = hubble_distance(cosmo.H0.value)
        return DH*1.0/np.sqrt(np.fabs(cosmo.Ok0))*np.sin(np.sqrt(np.fabs(cosmo.Ok0))*DC/DH)
    else:
        raise ValueError("omega curavture value not specified.")


def angular_diameter_distance(z,cosmo=None):
    """
    Calculate the angular diameter distance
    
    parameters
    ----------
    z: float
        redshift
    
    cosmo: astropy.cosmology object, optional
        cosmology object specifying cosmology.  If None,  FlatLambdaCDM(H0=70,Om0=0.3)
    
    returns
    -------
    DA: float
        Angular diameter distance in Mpc
    """

    if cosmo==None:
        cosmo = astropy.cosmology.FlatLambdaCDM(H0=70, Om0=0.3)

    return transverse_comoving_distance(z,cosmo)/(1.0+z)


def luminosity_distance(z,cosmo=None):
    """
    Calculate the luminosity distance.
    
    parameters
    ----------
    z: float
        redshift
    
    cosmo: astropy.cosmology object, optional
        cosmology object specifying cosmology.  If None,  FlatLambdaCDM(H0=70,Om0=0.3)
    
    returns
    -------
    DL: float
        Luminosity distance in Mpc
    """

    if cosmo==None:
        cosmo = astropy.cosmology.FlatLambdaCDM(H0=70, Om0=0.3)

    return transverse_comoving_distance(z,cosmo)*(1.0+z)


def comoving_volume(z,dw,cosmo=None):
    """
    Calculate comoving volume
    
    parameters
    ----------
    z: float
        redshift
    
    dw: float
        solid angle
    
    cosmo: astropy.cosmology object, optional
        cosmology object specifying cosmology.  If None,  FlatLambdaCDM(H0=70,Om0=0.3)
    
    returns
    -------
    VC: float
        comoving volume in Mpc^3
    """

    if cosmo==None:
        cosmo = astropy.cosmology.FlatLambdaCDM(H0=70, Om0=0.3)

    DH = hubble_distance(cosmo.H0.value) 
    f = lambda zz: DH*((1.0+zz)**2.0*angular_diameter_distance(zz,cosmo)**2.0)/(_Ez(zz, cosmo.Om0, cosmo.Ok0, cosmo.Ode0))

    VC = integrate.quadrature(f,0.0,z,vec_func=False)[0]*dw
    
    return VC


def _Ez(z, omega_m, omega_k, omega_l):
    """
    internal function used for distance calculations
    """
    return np.sqrt(omega_m*(1.0+z)**3.0+omega_k*(1.0+z)**2.0+omega_l)


