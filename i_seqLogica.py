'''
Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída serão apresentadas na execução do programa, seguindo a lógica do
exemplo abaixo. Para valores com mais de 6 dígitos, todos os dígitos devem ser apresentados
'''
x = int(input())

for y in range(1, (x + 1)):
	print(y, y * y, y ** 3)
	print(y, y * y + 1, y ** 3 + 1)