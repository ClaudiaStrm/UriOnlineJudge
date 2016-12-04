'''
Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.
'''

a = int(input())

for x in range(1, a+1):
	if x % 2 == 0:
		print("%d^2 = %d" %(x, x**2))