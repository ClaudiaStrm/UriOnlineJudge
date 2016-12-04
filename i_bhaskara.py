'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de 
Bhaskara. Se não for possível calcular as raízes, mostre a mensagem 
correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de 
numero negativo.
'''

   
bask = [float(x) for x in input().split()]

from math import sqrt

delta = bask[1] ** 2 - 4 * bask[0] * bask[2]
if bask[0] == 0 or delta <= 0:
	print("Impossivel calcular")
else:
	r1 = (- bask[1] + sqrt(delta)) / (2 * bask[0])
	print("R1 = %.5f" %r1)
	r2 = (- bask[1] - sqrt(delta)) / (2 * bask[0])
	print("R2 = %.5f" %r2)