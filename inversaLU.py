import numpy as np

def gaussCompacto(m):
	n = len(m)
	matrizInversa = np.zeros((n,n))
	vetorTemp = np.zeros(n)
	m_identidade = np.identity(len(m))
	controlaColuna = 0
	for j in range(0,n):
		for i in range(0,n):
			vetorTemp[i] = m_identidade[i][j]
		resultado = np.linalg.solve(m,vetorTemp)
		for p in range(0,n):
			matrizInversa[p][controlaColuna] = resultado[p]
		controlaColuna+=1
	print(matrizInversa)

def main():
	m = [[1,0,1],[0,1,2],[0,1,1]]
	d = np.linalg.det(m)
	if d==0:
		print("Matriz nao-inversivel!")
	else:
		gaussCompacto(m)
main()

