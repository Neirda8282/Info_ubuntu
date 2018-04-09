# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from pylab import *


X=[12,4,5,6]
Y=[1,3,7,9]
def Lx(i,x):
    P1,P2=1,1    
    for k in range(len(X)):
        if k!=i:
            P1=P1*(x-k)
            P2=P2*(i-k)
    return P1/P2

def polyx(t):
    R=0
    for k in range(len(X)):
        R+=Lx(k,t)*X[k]
    return R

def Ly(i,y):
    P1,P2=1,1    
    for k in range(len(Y)):
        if k!=i:
            P1=P1*(y-k)
            P2=P2*(i-k)
    return P1/P2

def polyy(t):
    R=0
    for k in range(len(Y)):
        R+=Ly(k,t)*Y[k]
    return R


plot(X,Y)

T=linspace(0,3,1000)
Xp,Yp=[],[]
for t in T:
    Xp.append(polyx(t))
    Yp.append(polyy(t))

plot(Xp,Yp)

show()            
    