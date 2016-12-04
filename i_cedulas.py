# -*- coding: utf-8 -*-
'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis 
(cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 
100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas 
necessárias.

'''
i, nt = 0, 0
vl = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
print(vl)
for x in notas:
	while vl >= notas[i]:
		vl = vl - notas[i]
		nt += 1	
	print ('%d nota(s) de R$ %d,00' %(nt, notas[i]))
	nt = 0
	i += 1


