'''
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
'''

num = int(input())
numhora = int(input())
valhora = float(input())

sal = numhora * valhora

print('NUMBER = %d\nSALARY = U$ %.2f' %(num, sal))