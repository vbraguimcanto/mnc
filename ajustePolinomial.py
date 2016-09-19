import numpy as np 
def somatorioXiYi(x,y,controlaXi):
	soma = 0
	for i in range(0,len(x)):
		soma = (x[i]**controlaXi)*y[i] + soma
	return soma

def somatorioXi(x,potencia):
	soma = 0
	for i in range(0,len(x)):
		soma = x[i]**potencia + soma
	return soma

def ajustePolinomial(x,y,grau):
	matrizCoeficientes = np.zeros((grau,grau))
	vetorY = np.zeros(grau)
	inicioLinhas = 1
	for i in range(0,grau):
		if i==1 or i==0:
			inicioLinhas+=0
		else:
			inicioLinhas+=1
		potencia = inicioLinhas
		for j in range(0,grau):
			if i==0 and j==0:
				matrizCoeficientes[i][j] = len(x)
			else:
				matrizCoeficientes[i][j] = somatorioXi(x,potencia)
				potencia+=1
		
	controlaXi = 1
	for i in range(0,grau):
		if i==0:
			vetorY[i] = sum(y)
		else:
			vetorY[i] = somatorioXiYi(x,y,controlaXi)
			controlaXi+=1

	resultado = np.linalg.solve(matrizCoeficientes,vetorY)
	print("Vetor Solução (a1, a2,...,an):")
	print(resultado)
def main():
    x = [-2, -1.5, 0.0, 1.0, 2.2, 3.1]
    y = [-30.5, -20.2, -3.3, 9.2, 16.8, 21.4]
    grau = int(input("Digite o grau desejado para o polinomio: "))
    ajustePolinomial(x,y,grau)
main()