'''
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores 
digitados são pares e mostre esta informação.
'''
i = 0
num = []
while i < 5:
	a = int(input())
	num.append(a)
	i+=1
i = 0
for x in num:
	if x % 2 == 0:
		i +=1
print('%d valores pares' %i)