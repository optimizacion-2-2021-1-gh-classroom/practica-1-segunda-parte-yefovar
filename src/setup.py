from distutils.core import setup
from setuptools import find_packages
 
setup(name = 'Simplex',
      version = '0.1',
      description = ' PAckage to solve Linear Programming problems using Simplex Algorithm',
      url = '',
      author = 'Equipo 3 MNO 2021',
      license = 'MIT',
      packages = find_packages(),
      install_requires = ['numpy','pandas','cython'],
      ext_modules = [Extension('SimplexC',['SimplexC/__init__.c'])]
      )

