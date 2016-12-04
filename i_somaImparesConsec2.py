'''
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. 7
Você deve apresentar a soma de todos os ímpares existentes entre X e Y.
'''


num = int(input())
lista = []
s = 0
for x in range(0, num):
	nota = [int(x) for x in input().split()]
	lista.append(nota)
	lista[x].sort()

for x in range(0, num):
	for y in range(lista[x][0], lista[x][1]):
		if y != lista[x][0] and y % 2 != 0:
			s += y
	print(s)
	s = 0