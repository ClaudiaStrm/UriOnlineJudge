'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
'''
peca1 = [float(x) for x in input().split()]
peca2 = [float(y) for y in input().split()]
total = (peca1[1] * peca1[2]) + (peca2[1] * peca2[2])

print('VALOR A PAGAR: R$ %.2f' %total)