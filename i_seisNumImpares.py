
'''
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser 
for o caso.
'''


a = int(input())

for x in range(a, a+12):
	if x % 2 != 0:
		print(x)