'''
Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou 
igual a 3.
'''

x = int(input())
y = int(input())

for x in range((min(x,y) + 1), max(x,y)):
	if x % 5 in (2,3):
		print(x)