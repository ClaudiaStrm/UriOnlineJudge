'''
Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.
'''

a = int(input())

for x in range(0, a+1):
	if x % 2 != 0:
		print(x)