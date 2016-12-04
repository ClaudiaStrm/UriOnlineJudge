#Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

x = int(input())
for z in range(1, (x + 1)):
	print(z, z ** 2, z ** 3)
