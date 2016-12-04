'''
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada 
par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).
'''

while True:

	lista = [int(x) for x in input().split()]
	lista.sort()
	seq = ''
	s = 0
	for x in range(lista[0], (lista[1] + 1)):
		seq = seq + str(x) + " "
		s += x

	if lista[0] <= 0 or lista[1] <=0:
		break
		
	print("%sSum=%d" %(seq, s))
