'''
Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o 
algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.
'''
y, z = 0, 0

while True:
	x = float(input())
	
	if x < 0 or x > 10:
		print("nota invalida")
	else:
		y += x
		z += 1
	if z == 2:
		break

print("media = %.2f" %(y / 2))
