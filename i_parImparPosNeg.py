'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram 
pares, quantos valores digitados foram ímpares, quantos valores digitados
foram positivos e quantos valores digitados foram negativos.
'''
i = 0
num = []
while i < 5:
	a = int(input())
	num.append(a)
	i+=1
i, j, k = 0, 0, 0
for x in num:
	if x % 2 == 0:
		i +=1
	if x > 0:
		j += 1
	elif x == 0:
		k += 1
		
print('%d valor(es) par(es)\n%d valor(es) impar(es)\n%d valor(es) positivo(s)\n%d valor(es) negativo(s)' %(i, (5 - i), j, (5 - j - k)))