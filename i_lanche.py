#-*- coding: utf-8 -*-
'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e 
a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
'''

qt = [int(x) for x in input().split()]
preco = [4, 4.5, 5, 2, 1.5]

total = qt[1] * preco[qt[0] - 1]

print('Total: R$ %.2f' %total)