import math as mt
import numpy as np
from scipy import *

def gaussSeidel(matrizInicial, vetorB, vetorAproxInicial, numIteracoes, erro):
    matrizA = np.tril(matrizInicial)
    matrizB = matrizInicial - matrizA
    j = 0
    for i in range(numIteracoes):
        vResultado = np.dot(np.linalg.inv(matrizA), vetorB - np.dot(matrizB, vetorAproxInicial))
        j+=1
        norma = np.linalg.norm(vResultado)
        if i != 0:
	        if mt.fabs(norma - tmp)/mt.fabs(norma) < erro:
	        	print "Iteracoes: ", j
	    		return vResultado
        tmp = norma
    print "Iteracoes: ", j
    return vResultado

def main():
	numIteracoes = int(input("Digite o numero maximo de iteracoes: "))
	erro = float(input("Digite o erro: "))
	matrizInicial = np.array([[9.0, 1.0, -2.0, 2.0], [1.0, -15.0, 3.0, 2.0], [1.0, -2.0, 8.0, 3.0], [2.0, 2.0, 1.0, 12.0]])
	vetorB = [10.5, 14.6, 18.1, 19.4]
	vetorAproxInicial = [1.0, 1.0, 1.0, 1.0]
	gaussSeidel(matrizInicial, vetorB, vetorAproxInicial, numIteracoes, erro)
	print np.linalg.solve(matrizInicial, vetorB)
main()
