#!/usr/bin/python
# -*- coding: utf8 -*-

import math

'''
Calcula el potencial y el campo electrico en el punto r para una dada configuracion
de i cargas Qi ubicadas en los puntos ri (con i desde 1 hasta el numero de cargas
Introduccion a la Fisica - Carrera de Fisica - UIS - Agosto 2013
'''
####################### mi clase vector
# Nuestra clase vector
class vector:
    def __init__(self,lista):
        self.x=[]
        for xi in lista:
          self.x.append(float(xi))
        self.dim=len(self.x)
        self.mod=math.sqrt(self.prod_escalar(self))

    def prod_escalar(self,a):
        if (self.dim == a.dim):
            pesc=0.
            for i in range(0,self.dim):
                pesc += (self.x[i] * a.x[i])
            return pesc
        else:
            print "El productor escalar se define para vectores de la misma dimension"
            return None

def suma(a, b):
    suma=[]
    if (a.dim == b.dim):
       for i in range(0,a.dim):
          suma.append(a.x[i]+b.x[i])
       return vector(suma)
    else:
       return None

def resta(a, b):
    resta=[]
    if (a.dim == b.dim):
       for i in range(0,a.dim):
          resta.append(a.x[i]-b.x[i])
       return vector(resta)
    else:
       return None

def vector_escalar(a, num):
    escalar=[]
    for i in range(0,a.dim):
      escalar.append(num*a.x[i])
    return vector(escalar)


################################## mi programa
# el codigo

# constante de Coulomb
k=8.988e9
# mis cargas
Q1 = 0.
r1 = vector([-1.0,0,0])
Q2 = +1.
r2=vector([0,0,0])
Q3 = 0.
r3=vector([1.0,0,0])
# y la carga de prueba
q = -1.;
#Defino los puntos iniciales para calcular la grilla xi,yi,zi y 
# los saltos, dx, dy y dz y el número de puntos nx,ny,nz
xi=-1.
xf=1.
dx=0.25
nx=int((xf-xi)/dx) + 1
yi=-1.
yf=1.
dy=0.25
ny=int((yf-yi)/dy) + 1
zi=-1.
zf=1.
dz=0.25
nz=int((zf-zi)/dz) + 1
for i in range(0,nx):
  x=xi+i*dx
  for j in range(0,ny):
    y=yi+j*dy
    for k in range(0,nz):
      z=zi+k*dz
      #establezco mi nueva posición en (x,y,z)
      r=vector([x,y,z])
      # recuerdo las definicions. Primero, calculo los vectores resta
      d1 = resta(r,r1)
      d2 = resta(r,r2)
      d3 = resta(r,r3)
      #Verifico que los vectores diferencia no sean nulos:
      if (d1.mod!=0. and d2.mod!=0. and d3.mod!=0.):
        # Calculo el potencial debido a cada carga en r
        V1 = -k*q*Q1/d1.mod
        V2 = -k*q*Q2/d2.mod
        V3 = -k*q*Q3/d3.mod
        # y ahora, segun el ppio de superposicion, el potencial total es
        V = V1 + V2 + V3
        # Ahora calculo el campo electrico (es una magnitud vectorial)
        # Calculo el campo electrico debido a cada carga individual
        # en vez de usar el vector unitario, uso el vector y divido por el
        # modulo al cubo
        E1 = vector_escalar(d1, k * q * Q1 / d1.mod**3)
        E2 = vector_escalar(d2, k * q * Q2 / d2.mod**3)
        E3 = vector_escalar(d3, k * q * Q3 / d3.mod**3)
        # Principio de superposicion: el campo electrico es
        E12 = suma(E1, E2)
        E = suma(E12,E3)
        # finalmente imprimo las coordenadas de r, 
        for i in range (0,r.dim):
          print r.x[i],
        # las coordenadas del campo electrico E(r)
        for i in range (0,r.dim):
          print E.x[i],
        # y el modulo del campo electrico |E(r)| y el potencial V(r)
        print E.mod,V
