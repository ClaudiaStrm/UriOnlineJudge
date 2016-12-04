'''
A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENAIS. 
Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever a mensagem "Novo grenal 
(1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número de gols 
marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).
'''

sn = 1
vinter, vgremio, empate, grenais = 0, 0, 0, 0
while sn == 1:
	inter, gremio = input().split()
	inter, gremio = int(inter), int(gremio)
	
	if inter > gremio:
		vinter +=1
	elif gremio > inter:
		vgremio += 1
	else:
		empate += 1

	grenais += 1
	sn = 0

	sn = int(input("Novo grenal (1-sim 2-nao)\n"))
	if sn != 1:
		break

print("%d grenais\nInter:%d\nGremio:%d\nEmpates:%d" %(grenais, vinter, vgremio, empate))
if vinter > vgremio:
	print("Inter venceu mais")
elif vgremio > vinter:
	print("Gremio venceu mais")
else:
	print("Nao houve vencedor")