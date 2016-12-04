'''
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.
'''

a = int(input())
b, c = 0, 0
lista = []
for x in range(0, a):
	x = int(input())
	lista.append(x)

for x in lista:
	if x in range(10,21):
		b += 1
	else:
		c += 1
print("%d in\n%d out" %(b, c))


