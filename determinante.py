import sys, math
def determinante(matriz, mult, tam):
    if tam == 1:
        return mult * matriz[0][0]
    else:
        sinal = -1
        valorDeterminante = 0
        for i in range(tam):
            aux = []
            for j in range(1, tam):
                v = []
                for p in range(tam):
                    if p != i:
                        v.append(matriz[j][p])
                aux.append(v)
            sinal *= -1
            valorDeterminante += mult * determinante(aux, sinal * matriz[0][i], len(aux))
        return valorDeterminante
def main():
	matriz = [[2,5,6],[1,6,7],[-1,2,3]]
	print 'Determinante:', determinante(matriz,1, len(matriz))
main()
