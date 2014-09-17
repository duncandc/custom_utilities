#Duncan Campbell
#Yale University
#July 22, 2014
#compile ckdtree code

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy

ext_modules = [Extension("pairs", ["pairs.pyx"])]
extra_compile_args=["-O3"]

setup(
  name = 'pairs app',
  #ext_modules = cythonize("pairs.pyx"),
  cmdclass = {'build_ext': build_ext},
  include_dirs=[numpy.get_include()],
  ext_modules = ext_modules
)

#to compile code type:
#    python setup_pairs.py build_ext --inplace