#Duncan Campbell
#March 2015
#Yale University
#code to do schechter function calculations.

import numpy as np
from scipy.special import gammainc as G #incomplete gamma function

__all__=['Schechter','Log_Schechter','Mag_Schechter','Double_Schechter','Log_Double_Schechter']

####single component schechter functions##################################################
class Schechter():
    
    def __init__(self, phi0, x0, alpha):
        self.phi0 = phi0
        self.x0 = x0
        self.alpha = alpha
    
    def __call__(self, x):
        x = np.asarray(x)
        x = x.astype(float)
        norm = self.phi0/self.x0
        val = norm * (x/self.x0)**self.alpha * np.exp(-x)
        return val
    
    def integrate(self,a,b):
        a = float(a)
        b = float(b)
        val = G(self.alpha+1.0,a/self.x0)-G(self.alpha+1.0,b/self.x0)
        return val

class Log_Schechter():
    
    def __init__(self, phi0, x0, alpha):
        self.phi0 = phi0
        self.x0 = x0
        self.alpha = alpha
    
    def __call__(self, x):
        x = np.asarray(x)
        x = x.astype(float)
        norm = np.log(10.0)*self.phi0
        val = norm*(10.0**((x-self.x0)*(1.0+self.alpha)))*np.exp(-10.0**(x-self.x0))
        return val

class Log_Super_Schechter():
    
    def __init__(self, phi0, x0, alpha1, alpha2):
        self.phi0 = phi0
        self.x0 = x0
        self.alpha1 = alpha1
        self.alpha2 = alpha2
    
    def __call__(self, x):
        x = np.asarray(x)
        x = x.astype(float)
        norm = np.log(10.0)*self.phi0
        val = norm*(10.0**((x-self.x0)*(1.0+self.alpha1)))*np.exp(-10.0**(self.alpha2*(x-self.x0)))
        return val

class Mag_Schecter():
    
    def __init__(self, phi0, m0, alpha):
        self.phi0 = phi0
        self.m0 = m0
        self.alpha = alpha
    
    def __call__(self, x):
        x = np.asarray(x)
        x = x.astype(float)
        norm = (2.0/5.0)*self.phi0*np.log(10.0)
        val = norm*(10.0**(2.5*(self.m0-x)))**(self.alpha+1.0)*np.exp(-10.0**(2.5*(self.m0-x)))
        return val


####double component schechter functions##################################################
class Double_Schechter():
    
    def __init__(self, x0, phi1, phi2, alpha1, alpha2):
        self.phi1 = phi1
        self.phi2 = phi2
        self.x0 = x0
        self.alpha1 = alpha1
        self.alpha2 = alpha2
    
    def __call__(self, x):
        x = np.asarray(x)
        x = x.astype(float)
        norm = self.x0
        val = norm * np.exp(-x)* (self.phi1*(x/self.x1)**self.alpha1 +\
                                  self.phi2*(x/self.x2)**self.alpha2)
        return val

class Log_Double_Schechter():
    
    def __init__(self, x1, x2, phi1, phi2, alpha1, alpha2):
        self.phi1 = phi1
        self.phi2 = phi2
        self.x1 = x1
        self.x2 = x2
        self.alpha1 = alpha1
        self.alpha2 = alpha2
    
    def __call__(self, x):
        x = np.asarray(x)
        x = x.astype(float)
        norm = np.log(10.0)
        val = norm *\
              (np.exp(-10.0**(x - self.x1)) * 10.0**(x - self.x1) *\
                   self.phi1 * (10.0**((x - self.x1) * self.alpha1)) +\
               np.exp(-10.0**(x - self.x2)) * 10.0**(x - self.x2) *\
                   self.phi2 * (10.0**((x - self.x2) * self.alpha2)))
        return val


####triple component schechter functions##################################################
class Log_Triple_Schechter():
    
    def __init__(self, x1, x2, x3, phi1, phi2, phi3, alpha1, alpha2, alpha3):
        self.phi1 = phi1
        self.phi2 = phi2
        self.phi3 = phi3
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.alpha1 = alpha1
        self.alpha2 = alpha2
        self.alpha3 = alpha3
    
    def __call__(self, x):
        x = np.asarray(x)
        x = x.astype(float)
        norm = np.log(10.0)
        val = norm *\
              (np.exp(-10.0**(x - self.x1)) * 10.0**(x - self.x1) *\
                   self.phi1 * (10.0**((x - self.x1) * self.alpha1)) +\
               np.exp(-10.0**(x - self.x2)) * 10.0**(x - self.x2) *\
                   self.phi2 * (10.0**((x - self.x2) * self.alpha2)) +\
               np.exp(-10.0**(x - self.x3)) * 10.0**(x - self.x3) *\
                   self.phi3 * (10.0**((x - self.x3) * self.alpha3)))
        return val

