import math as mt
import numpy as np
from scipy import *

def jacobiRichardson(matrizInicial, vetorB, vetorAproxInicial, numIteracoes, erro):
    matrizA = np.diag(matrizInicial)
    matrizB = matrizInicial - np.diagflat(matrizA)
    j = 0
    for i in range(numIteracoes):
    	vetorAproxInicial = (vetorB - np.dot(matrizB,vetorAproxInicial))/matrizA
    	j+=1
    	norma = np.linalg.norm(vetorAproxInicial)
    	if i != 0:
	        if mt.fabs(norma - tmp)/mt.fabs(norma) < erro:
	        	print "Iteracoes: ", j
	    		return vetorAproxInicial
        tmp = norma
	print "Iteracoes: ", j
	return vetorAproxInicial

def main():
	numIteracoes = int(input("Digite o numero maximo de iteracoes: "))
	erro = float(input("Digite o erro: "))
	matrizInicial = np.array([[10.0, 2.0, 1.0], [1.0, 5.0, 1.0], [2.0, 3.0, 10.0]])
	vetorB = [7.0, -8.0, 6.0]
	vetorAproxInicial = [0.7, -1.6, 0.6]
	vetorAproxInicial = jacobiRichardson(matrizInicial, vetorB, vetorAproxInicial, numIteracoes, erro)
	print np.linalg.solve(matrizInicial, vetorB)
main()
