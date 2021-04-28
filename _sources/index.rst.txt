.. Simplex documentation master file, created by
   sphinx-quickstart on Fri Mar 19 19:20:16 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentacion del paquete Simplex!
===================================

Este paquete se utiliza para resolver problemas de maximización y minimización de Programación Lineal utilizando el método Simplex. 

Imagenes de Docker
==================
Se cuentan con dos imagenes de Docker que permiten la utilización de este paquete. 
El paquete `yalidt/pkg_optimizacion:0.1 <https://hub.docker.com/r/yalidt/pkg_optimizacion/tags?page=1&ordering=last_updated>`_ contiene 
un Jupyter Notebook con la paquetería instalada.

Si se desea hacer uso de Kale y Kubeflow, se recomeinda instalar esta imagen `ferubio/pkg_optim_kale:0.1 <https://hub.docker.com/r/ferubio/pkg_optim_kale>`_

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Problema de Maximización
========================
Problema de maximización de una función objetivo lineal con restricciones:
   :math:`\max_x (-c)^Tx`\
   
   :math:`S.A`\
   
   :math:`Ax\leq b`\
  
   :math:`x \geq 0`\

   Con: 
   
   :math:`c,x \in \mathbb{R}^n`\
   
   :math:`A \in \mathbb{R}^{m \times n}`\
   
   :math:`b\in \mathbb{R}^m`\
   
Problema de Minimización
========================
Problema de minimización de una función objetivo lineal con restricciones:
   :math:`\min_x c^Tx`\
   
   :math:`S.A`\
   
   :math:`Ax\geq b`\
  
   :math:`x \geq 0`\

   Con: 
   
   :math:`c,x \in \mathbb{R}^n`\
   
   :math:`A \in \mathbb{R}^{m \times n}`\
   
   :math:`b\in \mathbb{R}^m`\

.. toctree::
   :maxdepth: 2
   :caption: Contents:

