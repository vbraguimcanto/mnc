import math as mt

def ajusteReta(x,y):
	xi_yi = 0
	xi_q = 0
	for i in range(0, len(x)):
		xi_yi = x[i]*y[i]+xi_yi
		xi_q = mt.pow(x[i],2)+xi_q
	a = (len(x)*xi_yi - sum(x)*sum(y))/(len(x)*xi_q - sum(x)*sum(x))
	b = (sum(y) - len(x) * sum(x))/(len(x))
	print(a)
	print(b)

def main():
    x = [-2,-0.5, 1.2, 2.1, 3.5, 5.4]
    y = [4.4, 5.5, 3.2, 1.6, 0.6, -0.6]
    ajusteReta(x,y)
main()