from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name = 'sphere_dist_fast app',
    ext_modules = cythonize("sphere_dist_fast.pyx"),
    include_dirs = [np.get_include()], 
)

#to compile cython code type: python setup.py build_ext --inplace
