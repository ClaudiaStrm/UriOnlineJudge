'''
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto 
escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação 
sem escrever mensagem alguma).
'''
'''

2 2 primeiro
3 -2 segundo
-8 -1 terceiro
-7 1 quarto
'''

while True:
	x, y = input().split()
	x, y = int(x), int(y)

	if x > 0 and y > 0:
		print("primeiro")
	elif x > 0 and y < 0:
		print("quarto")
	elif x < 0 and y < 0:
		print("terceiro")
	elif x < 0 and y > 0:
		print("segundo")

	if x == 0 or y == 0:
		break