import sys, math
def f(x):
	return math.log(x)
def dfdx(xk,h):
	return (f(xk + h) - f(xk))/h
def dfdx2(xk,h):
	return dfdx(xk,h) - dfdx(xk,-h)/2*h
def main():
	ponto = float(input("Digite o ponto: "))
	h = float(input("Digite o valor de H: "))
	print 'Derivada Segunda Aproximada:',
	print dfdx2(ponto,h)
main()
