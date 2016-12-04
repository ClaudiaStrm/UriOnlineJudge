#Escreva um programa que leia dois valores X e Y. A seguir, mostre uma sequência de 1 até Y, passando para a próxima linha a cada X 
#números.
'''
import math

x = int(input())
y = int(input())
lista = []
a, b = 0, x
loop = math.ceil(y / x) 

for z in range(1, (y+1)):
	lista.append(z)

for z in range(0, loop):
	print(lista[a:b])
	a = b
	b = b + x
'''

x, y = input().split()
x, y = int(x), int(y)
a = 1
while a <= y:	
	for z in range(1, x):
		if a == y:
			print(a)
		if a < y:
			print(a, end=" ")	
		a+=1	
	if a <=y:
		print(a)
	a += 1
