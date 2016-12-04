'''
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, 
deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a 
primeira letra maiúscula.
'''

mes = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
num = int(input()) 
num -= 1
print(mes[num])
