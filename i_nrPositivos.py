'''Faça um programa que leia 6 valores. Estes valores serão somente negativos 
ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de 
valores positivos digitados
'''
nr = []
x = 0
p = 0

while x < 6:
	i = float(input())
	nr.append(i) 
	x+=1

for x in nr:
	if x >= 0:
		p += 1

print('%d valores positivos' %p)