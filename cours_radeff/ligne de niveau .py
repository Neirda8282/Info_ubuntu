from numpy import * 
from pylab import *

def f(u):
    x,y=u[0],u[1]
    res=x**2+2*y**2+2*x*y
    return res

def nablaf(u):
    x,y=u[0],u[1]
    X=2*x+2*y
    Y=4*y+2*x
    res=array([X,Y])
    return res

def Vunit(u):
    x,y=u[0],u[1]
    n=nablaf(u)
    v=array([-n[1],n[0]])
    v=v/sqrt(dot(v,v))
    return v

def points(n,pas,u):
    A=[u]
    K=f(u)
    for k in range(n):
        Vt=Vunit(A[k])
        ik=pas*Vt
        Lambda=K-f(ik)/dot(nablaf(ik),nablaf(ik))
        Ak=ik+Lambda*nablaf(ik)
        A.append(Ak)
    return array(A)

def affichage(A):
    n,p=A.shape
    x,y=[],[]
    for j in range(n):
        x.append(A[j][0])
        y.append(A[j][1])

    plot(x,y)
    show()

affichage(points(10,0.5,array([1,0])))