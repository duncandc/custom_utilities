__all__=["chisqg","redchisqg"]

"""
Computing the chi-squared and reduced chi-squared of a model. Code taken from 
http://astropython.blogspot.com/2012/02/computing-chi-squared-and-reduced-chi.html
"""


import numpy as np

def chisqg(ydata, ymod, sd=None):
    """ 
    Chi-square error statistic
    
    Parameters
    ==========
    ydata: array_like
        data values
    
    ymod: array_like
        model values
    
    sd: array_like, optional
        standard deviations of data points
    
    Returns
    =======
    chisq: float
    
    Notes
    =====
    Returns the chi-square error statistic as the sum of squared errors between
    Ydata(i) and Ymodel(i). If individual standard deviations (array sd) are supplied,
    then the chi-square error statistic is computed as the sum of squared errors
    divided by the standard deviations. Inspired on the IDL procedure linfit.pro.
    See http://en.wikipedia.org/wiki/Goodness_of_fit for reference.
   
    Rodrigo Nemmen  
    http://goo.gl/8S1Oo  
    """
    
    # Chi-square statistic (Bevington, eq. 6.9)  
    if sd==None:  
        chisq=np.sum((ydata - ymod)**2.0)  
    else:  
        chisq=np.sum(((ydata - ymod) / sd)**2.0)  
    
    return chisq


def redchisqg(ydata, ymod, deg=2, sd=None):  
    """ 
    Reduced chi-square error statistic.
    
    Parameters
    ==========
    ydata: array_like
        data values
    
    ymod: array_like
        model values
    
    deg: integer
        number of degrees of freedom in the model
    
    sd: array_like, optional
        standard deviations of data points
    
    Returns
    =======
    chisq: float
    
    Notes
    =====
    Returns the reduced chi-square error statistic for an arbitrary model,
    chisq/nu, where nu is the number of degrees of freedom. If individual
    standard deviations (array sd) are supplied, then the chi-square error
    statistic is computed as the sum of squared errors divided by the standard
    deviations. See http://en.wikipedia.org/wiki/Goodness_of_fit for reference.
   
    Usage:
    >>> chisq=redchisqg(ydata,ymod,n,sd)
       
    Rodrigo Nemmen  
    http://goo.gl/8S1Oo  
    """
    
    # Chi-square statistic  
    if sd==None:
        chisq=np.sum((ydata - ymod)**2.0)
    else:
        chisq=np.sum(((ydata - ymod) / sd)**2.0)
    
    # Number of degrees of freedom assuming 2 free parameters  
    nu= ydata.size - 1 - deg
    
    return chisq/nu 


