## Práctica 1, 2da parte

Integrantes del equipo:

| usuario   | Rol               | Persona      | Actividad   |
| --------- | ------------------| ------------|--------------|
| jreyesgar93| Project Manager/Programación     | José        | Pruebas del software/Documentación|
| yalidt    | Programación/Revisión   | Yalidt      | Dockerfile/Docker hub actions/ Botón Binder|
| yefovar   | Programación/Documentación  | Yedam          | Implementación del algoritmo/Pruebas Unitarias |
| mfrubio   | Programación/Revisión        | Fernanda    | Revisión Docker|

## Paquete Simplex
Implementamos un paquete en Python que resuelve problemas de maximización de una función objetivo lineal con restricciones:

![equation](https://latex.codecogs.com/gif.latex?max_{x}\quad&space;c^{T}x) 

sujeto a:

![equation](https://latex.codecogs.com/gif.latex?Ax\leq&space;b)

![equation](https://latex.codecogs.com/gif.latex?x\geq&space;0) 

con:

![equation](https://latex.codecogs.com/gif.latex?c,x\quad\epsilon\quad\mathbb{R}^{n})

![equation](https://latex.codecogs.com/gif.latex?A\quad\epsilon\quad\mathbb{R}^{m\times&space;n})

![equation](https://latex.codecogs.com/gif.latex?b\quad\epsilon\quad\mathbb{R}^{m})

Usamos sphynx para documentar nuestro [paquete.](https://optimizacion-2-2021-1-gh-classroom.github.io/practica-1-segunda-parte-yefovar/Simplex.html#module-Simplexs)

Además cuenta con un módulo con código optimizado en C llamado SimplexC
### Botón de binder 
Para consultar ejemplos de implementaciones usa el boton de binder y el notebook para realizar el *testing* es PruebaBinder.ipynb que se encuentra en el siguiente directorio: `home/jovian/practica-1-segunda-parte-yefovar`

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-yefovar/main?urlpath=lab)


## Organización del repositorio

```bash
   practica-1-segunda-parte-yefovar/
├── 3_parte_2_practica_1.ipynb
├── Dockerfile
├── README.md
├── dockerfiles
│   └── pkg
│       └── Dockerfile
├── instrucciones.ipynb
├── old_README.md
├── requirements.txt
└── src
    ├── Simplex
    │   └── __init__.py
    ├── SimplexC
    │   ├── __init__.c
    │   ├── __init__.cpython-39-x86_64-linux-gnu.so
    │   ├── __init__.html
    │   └── __init__.pyx
    ├── build
    │   ├── lib.linux-x86_64-3.9
    │   │   └── SimplexC
    │   │       └── __init__.cpython-39-x86_64-linux-gnu.so
    │   └── temp.linux-x86_64-3.9
    │       └── SimplexC
    │           └── __init__.o
    ├── docs
    │   ├── Makefile
    │   ├── Simplex.rst
    │   ├── SimplexC.rst
    │   ├── conf.py
    │   ├── index.rst
    │   ├── make.bat
    │   └── modules.rst
    ├── setup.py
    └── tests
        ├── requirements.txt
        ├── test.py
        └── tests_simpexc.py

13 directories, 27 files
```

## Evidencia trabajo AWS

Se anexa evidencia de trabajo y solución del problema a través de cómputo en la nube.

<img src="https://github.com/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-yefovar/blob/main/images/aws%20-%201.png">

<img src="https://github.com/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-yefovar/blob/main/images/aws%20-%202.png">

