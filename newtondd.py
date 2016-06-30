import numpy as np
import math as mt

def newton(vetorX, vetorY, x, grau):
    n = len(vetorX)
    v = np.zeros((n,n))
    for j in range(n):
        v[j,0] = vetorY[j]           
    for i in range(1,n):        
        for j in range(n-i):   
            v[j,i] = (v[j+1,i-1]-v[j,i-1])/(vetorX[j+i]-vetorX[j])
    P = v[0,0]
    for i in range(1,n):
        P = v[0,i]*(mt.pow(x,i) - 1) + P
    return P 
def main():
    vetorX = [1.0,-1.0,-2.0]
    vetorY = [0.0,-3.0,-4.0]
    x = float(input("Digite o valor do ponto x: "))
    grau = int(input("Digite o valor do grau polinomio: "))
    P = newton(vetorX,vetorY,x,grau)
    print P    
main()
