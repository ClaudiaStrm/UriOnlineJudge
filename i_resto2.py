'''
Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.
'''

a = int(input())

for i in range(1, 10000):
	if i % a == 2:
		print(i)