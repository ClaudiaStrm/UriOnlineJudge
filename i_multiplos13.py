'''Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo 
ambos.
'''

x = int(input())
y = int(input())
soma = 0

for x in range(min(x,y), (max(x,y) + 1)):
	if x % 13 != 0:
		soma += x

print(soma)
