#Autores: 
#Hugo Rodrigues da Silva
#Maria Luiza Rodrigues da Silva


import numpy
from scipy import linalg

def matriz_A(n_linha):
    Matriz = []
    y = 1
    while len(Matriz) != n_linha:
        print('insira os elementos da linha', y)
        y = y+1
        n = input('>: ').split(' ')
        Matriz.append(n)
        n = []
    return Matriz

def matriz_b():
    Matriz = []
    print('insira os elementos da matriz b: ')
    n = input('>: ').split(' ')
    Matriz.append(n)
    n = []
    return Matriz

incognitas = int(input("nº de incógnitas: "))
A = matriz_A(incognitas)
b = matriz_b()
b_matriz = numpy.array(b)
b_transposta = numpy.transpose(b_matriz)
matriz_X = linalg.solve(A, b_transposta)
print("Matriz X: ")
print(matriz_X)



