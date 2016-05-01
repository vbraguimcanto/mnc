import sys, math
def f(x):
	return x**2 + math.log(x)
def dfdx(xk,h):
	return (f(xk + h) - f(xk))/h
def newton(xa,xb,numeroIteracoes,erro,aproxInicial):
	xk = aproxInicial - (f(aproxInicial)/dfdx(aproxInicial,0.01))
	for i in range(numeroIteracoes):		
		if (xb-xa)/xb < erro:
			return xk
		xAnterior = xk
		xk = xAnterior - (f(xAnterior)/dfdx(xAnterior,0.01))
	return xk
def main():
	a = float(input("Digite o valor de xa: "))
	b = float(input("Digite o valor de xb: "))
	numeroIteracoes = int(input("Digite o numero de iteracoes: "))
	erro = float(input("Digite o erro: "))
	aproxInicial = float(input("Digite a aproximacao inicial: "))
	print 'Raiz Aproximada:',
	print newton(a,b,numeroIteracoes,erro,aproxInicial)
main()
