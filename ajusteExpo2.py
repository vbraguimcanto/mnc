import math as mt
import numpy as np

def ajusteExpo2(x,y):
	xi_lnyi = 0
	lnyi = 0
	xi_q = 0
	for i in range(0, len(x)):
		xi_lnyi = x[i]* np.log(y[i]) + xi_lnyi
		lnyi = np.log(y[i]) + lnyi
		xi_q = mt.pow(x[i],2) + xi_q
	a = (len(x)*xi_lnyi - sum(x)*lnyi)/(len(x)*xi_q - sum(x)*sum(x))
	b = (lnyi - a*sum(x))/len(x)
	b = mt.exp(1)**b
	print(a)
	print(b)

def main():
    x = [0.10, 1.50, 3.30, 4.50, 5.00]
    y = [1.77, 2.17, 2.48, 2.99, 3.15]
    ajusteExpo2(x,y)
main()