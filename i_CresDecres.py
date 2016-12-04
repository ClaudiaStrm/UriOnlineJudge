'''
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores
foram digitados em ordem crescente ou decrescente
'''
while True:

	lista = [int(x) for x in input().split()]

	if lista[0] < lista[1]:
		print("Crescente")
	if lista[0] > lista[1]:
		print("Decrescente")
	if lista[0] == lista[1]:
		break