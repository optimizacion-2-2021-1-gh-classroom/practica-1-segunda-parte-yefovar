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

### Botón de binder 
Para consultar ejemplos de implementaciones usa el boton de binder y el notebook para realizar el *testing* es PruebaBinder.ipynb que se encuentra en el siguiente directorio: `home/jovian/practica-1-segunda-parte-yefovar`

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-yefovar/main?urlpath=lab)


## Organización del repositorio

```bash
    .
    ├── README.md
    ├── dockerfiles     
    │   └── pkg
    │   	└── Dockerfile
    ├── src     
    │   ├── Simplex
    │   │	└── __init__.py
    │   ├── docs
    │   │	├── Makefile
    │   │   ├── Simplex.rst
    │   │   ├── conf.py
    │   │   ├── index.rst
    │   │   ├── make.bat
    │   │   └── modules.rst
    │   ├── test
    │   │   ├── Simplex.py
    │   │   ├── requirements.txt
    │   │   └── test.py
    │   └── setup.py
    ├── Dockerfile
    ├── PruebaBinder.ipynb
    ├── instrucciones.ipynb
    └── old_README.md

3 directories, 16 files
```

## Evidencia trabajo AWS

Se anexa evidencia de trabajo y solución del problema a través de cómputo en la nube.

<img src="https://github.com/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-yefovar/blob/main/images/aws%20-%201.png">

<img src="https://github.com/optimizacion-2-2021-1-gh-classroom/practica-1-segunda-parte-yefovar/blob/main/images/aws%20-%202.png">

