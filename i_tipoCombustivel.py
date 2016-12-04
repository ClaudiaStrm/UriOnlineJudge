'''
Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o 
tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código 
inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código 
informado for o número 4.
'''

x = 0
alcool, gasolina, diesel = 0, 0, 0

while x != 4:
	x = int(input())
	if x == 1:
		alcool += 1
	elif x == 2:
		gasolina += 1
	elif x == 3:
		diesel += 1
print("MUITO OBRIGADO\nAlcool: %d\nGasolina: %d\nDiesel: %d" %(alcool, gasolina, diesel))
