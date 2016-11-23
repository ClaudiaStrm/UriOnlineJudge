'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
'''

x = [float(y) for y in input().split()]
a = x[0]
b = x[1]
c = x[2]

if a > b and a > c:
	m = a
elif b > c:
	m = b
else:
	m = c
print("%d eh o maior" %m)