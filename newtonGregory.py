import numpy as np
import math as mt

def newtonGregory(vetorX, vetorY, x, grau):
    h = mt.fabs(vetorX[1] - vetorX[0])
    n = len(vetorX)
    v = np.zeros((n,n))
    for j in range(n):
        v[j,0] = vetorY[j]           
    for i in range(1,n):        
        for j in range(n-i):   
            v[j,i] = (v[j+1,i-1]-v[j,i-1])
    s = (x - vetorX[0])/h
    P = v[0,0]
    for i in range(1,n):
        aux = 1.0
        for j in range(i):
            aux = aux * (s - j)
        P = (v[0,i]*aux)/(mt.factorial(i)) + P
    print v
    return P 
def main():
    vetorX = [110.0,120.0,130.0]
    vetorY = [2.041,2.079,2.114]
    x = float(input("Digite o valor do ponto x: "))
    grau = int(input("Digite o valor do grau polinomio: "))
    P = newtonGregory(vetorX,vetorY,x,grau)
    print P    
main()
