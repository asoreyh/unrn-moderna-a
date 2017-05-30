#!/usr/bin/python
# -*- coding: utf8 -*-

import math
import sys

####################### mi clase vector

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

k=8.988

Q=[]
ri=[]
import sys

if (len(sys.argv) != 3):
  sys.exit("error: python charges.py <num-of-charges> <lim>")


dq=float(sys.argv[1])
N=int(dq)


if (N==1):
    Q.append(-1.0)
    ri.append(vector([0.0,0.0,0.0]))
else:
  for i in range(-N/2,N/2+1):
    Q.append(1.0)
    ri.append(vector([i/dq,0.5,0]))
    Q.append(-1.0)
    ri.append(vector([i/dq,-0.5,0]))

q=5e-2/dq
res=2.
dr = 1./res
lim = float(sys.argv[2])

for x in range(int(-lim*res),int((lim*res)+1)):
  for y in range(int(-lim*res),int((lim*res)+1)):
    for z in range(int(-lim*res),int((lim*res)+1)):
      r=vector([x*dr,y*dr,z*dr])
      F=vector([0,0,0])
      for i in range(0,len(Q)):
        di=resta(r,ri[i])
        if (di.mod):
          Ei_mod = k*Q[i] / di.mod**3
          Ei = vector_escalar(di,Ei_mod)
          Fi = vector_escalar(Ei,q)
          F=suma(F,Fi)
      for i in range (0,r.dim):
        print r.x[i],
      for i in range (0,r.dim):
        print F.x[i],
      print F.mod
