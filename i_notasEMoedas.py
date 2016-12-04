'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor 
representa um valor monetário. A seguir, calcule o menor número de notas e 
moedas possíveis no qual o valor pode ser decomposto. As notas consideradas 
são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 
0.05 e 0.01. A seguir mostre a relação de notas necessárias.
'''


i, nt = 0, 0
vl = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
print('NOTAS:')
for x in notas:
	while vl >= notas[i]:
		vl = vl - notas[i]
		nt += 1	
	print ('%d nota(s) de R$ %d.00' %(nt, notas[i]))
	nt = 0
	i += 1
i, nt = 0, 0
print("MOEDAS:")
for x in moedas:
	while vl + 0.001 >= moedas[i]:
		nt +=1
		vl = vl - moedas[i]
	print('%d moeda(s) de R$ %.2f' %(nt, moedas[i]))
	nt = 0
	i += 1