'''
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.
'''

lista = []
i, j = 1, 0
for x in range(0, 100):
	x = int(input())
	lista.append(x)
print(max(lista))
while lista[j] < max(lista):
	i += 1
	j += 1
print(i)

