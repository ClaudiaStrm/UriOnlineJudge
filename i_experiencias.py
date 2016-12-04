'''
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um 
laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de 
cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o 
número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.
'''
num = int(input())
c, r, s = 0, 0, 0
total = 0
lista = []
pc = '%'
for x in range(0, num):
	nota = [	(x) for x in input().split()]
	lista.append(nota)
for x in range(0, num):
	total = total + int(lista[x][0])
	if lista[x][1] == "C":
		c = c + int(lista[x][0])
	elif lista[x][1] == "R":
		r = r + int(lista[x][0])
	else:
		s = s + int(lista[x][0])
print('Total: %d cobaias \nTotal de coelhos: %d \nTotal de ratos: %d \nTotal de sapos: %d \nPercentual de coelhos: %.2f %s \nPercentual de ratos: %.2f %s \nPercentual de sapos: %.2f %s\n' %(total, c, r, s, (c * 100 / total), pc, (r * 100 / total), pc, (s * 100 / total), pc))
