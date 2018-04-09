from random import randint
from time import clock
from pylab import *
def echange(A,i,j):
    A [i],A[j]=A[j],A[i]

def partition(A,g,d):
    pivot,m=A[g],g
    for i in range(g+1,d):
        if A[i]<=pivot:
            echange(A,i,m+1)
            m=m+1
    echange(A,m,g)
    return m

def tri_rec(A,n,p):
    if n<p:
        m=partition(A,n,p)
        tri_rec(A,n,m)
        tri_rec(A,m+1,p)

def tri_rapide(A):
    tri_rec(A,0,len(A))


A=['ee','aa','zz','rr','cc','ww','bb','kk','jj']

def temps_calcul(n):
    A=[randint(0,5000) for k in range(n)] #liste a trier
    t1=clock()
    tri_rapide(A)
    t1=clock()-t1
    return (t1/(n*log(n)))

X=[100,1000,2000,7000,20000]
Y=[temps_calcul(n) for n in X]



plot(X,Y)
show()

