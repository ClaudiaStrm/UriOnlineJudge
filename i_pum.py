#Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

x = int(input())
pum = 1

for y in range(0,x):
	print("%d %d %d PUM" %(pum, (pum + 1), (pum + 2)))
	pum += 4