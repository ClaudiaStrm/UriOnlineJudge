'''
Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostre a 
mensagem “divisao impossivel” para os valores em questão.
'''
num = int(input())
for n in range(0, num):
	x, y = input().split()
	x, y = int(x), int(y)

	if y == 0:
		print("divisao impossivel")
	else:
		print("%.1f" %(x / y))