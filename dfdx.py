# Algoritmo para calcular a primeira derivada
# Desenvolvido por Victor Hugo Braguim Canto
# Disciplina de Métodos Numéricos Computacionais
# Universidade Estadual Paulista - UNESP

import sys, math
def f(x):
	return math.log(x)
def dfdx(xk,h):
	return (f(xk + h) - f(xk))/h
def main():
	ponto = float(input("Digite o ponto: "))
	h = float(input("Digite o valor de h: "))
	print 'Derivada Primeira Aproximada:',
	print dfdx(ponto,h)
main()
