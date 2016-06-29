import numpy as np
 
def lagrange(p, x, vetorX, tamVetorX, grau):
  valorAuxLagrange = 1.0
  for i in xrange(tamVetorX):
    if (i != p):
      valorAuxLagrange = valorAuxLagrange * ( (x - vetorX[i]) / (vetorX[p] - vetorX[i]) )
  return valorAuxLagrange

def main():
	valorPolinomioLagrange = 0
	vetorX = np.array([1.0, 3.0, 4.0, 5.0])
	vetorY = np.array([0.0, 6.0, 24.0, 60.0])
	x = float(input("Digite o valor do ponto x: "))
	grau = int(input("Digite o valor do grau polinomio: "))
	tamVetorX  = len(vetorX)
	for i in range(tamVetorX):
	  valorPolinomioLagrange = valorPolinomioLagrange + vetorY[i]*lagrange(i, x, vetorX, tamVetorX, grau)
	print valorPolinomioLagrange
main()
