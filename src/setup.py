
from setuptools import setup, find_packages
 
setup(name = 'Simplex',
      version = '0.1',
      description = ' PAckage to solve Linear Programming problems using Simplex Algorithm',
      url = '',
      author = 'Equipo 3 MNO 2021',
      license = 'MIT',
      packages = find_packages(),
      install_requires = ['numpy','pandas','nose','networkx']
      )

