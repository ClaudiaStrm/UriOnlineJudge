'''
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente,
de modo que o lado A representa o maior dos 3 lados. A seguir, determine o
tipo de triângulo que estes três lados formam, com base nos seguintes casos, 
sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
'''

val = [float(x) for x in input().split()]
val.sort(reverse=True)

A = val[0]
B = val[1]
C = val[2]

if A >= B + C:
	print('NAO FORMA TRIANGULO')
else:
	if A ** 2 == B ** 2 + C** 2:
		print('TRIANGULO RETANGULO')
	if A ** 2 > B ** 2 + C ** 2: 
		print('TRIANGULO OBTUSANGULO')
	if A ** 2 < B ** 2 + C**2:
		print('TRIANGULO ACUTANGULO')
	if A == B == C:
		print('TRIANGULO EQUILATERO')
	elif A == B or A == C or C == B:
		print('TRIANGULO ISOSCELES')
