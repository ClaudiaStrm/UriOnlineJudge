'''
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos
 os valores positivos digitados, com um dígito após o ponto decimal.
 '''
lista = []
for x in range(6):
	x = float(input())
	lista.append(x)
pos = []
m, p = 0, 0
for x in lista:
	if x > 0:
		p += 1
		m += x
print("%d valores positivos\n%.1f" %(p, m/p))
