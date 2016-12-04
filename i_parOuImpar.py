'''
Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada valor lido, mostre uma mensagem 
em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a 
zero (0), embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá imprimir apenas NULL.
'''


a = int(input())
b, c = 0, 0
lista = []
for x in range(0, a):
	x = int(input())
	lista.append(x)

for x in lista:
	if x == 0:
		print("NULL")
	elif x > 0 and x % 2 == 0:
		print("EVEN POSITIVE")
	elif x < 0 and x % 2 == 0:
		print("EVEN NEGATIVE")
	elif x > 0 and x % 2 != 0:
		print("ODD POSITIVE")
	else:
		print("ODD NEGATIVE")