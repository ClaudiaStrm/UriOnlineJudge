'''
Escreva um programa para ler as notas da primeira e a segunda avaliação de um aluno. Calcule e imprima a média semestral. O programa só 
deverá aceitar notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

No final deve ser impressa a mensagem “novo calculo (1-sim 2-nao)”, solicitando ao usuário que informe um código (1 ou 2) indicando se 
ele deseja ou não executar o algoritmo novamente, (aceitar apenas os código 1 ou 2). Se for informado o código 1 deve ser repetida a 
execução de todo o programa para permitir um novo cálculo, caso contrário o programa deve ser encerrado.
'''

sn = 1
while sn == 1:
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
	sn = 0
	while True:
		sn = int(input("novo calculo (1-sim 2-nao)\n"))
		if sn == 1 or sn == 2:
			break
	if sn == 2:
		break