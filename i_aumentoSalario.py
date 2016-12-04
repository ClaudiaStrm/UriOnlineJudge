'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de 
acordo com a tabela abaixo:
Leia o salário do funcionário e calcule e mostre o novo salário, bem como o 
valor de reajuste ganho e o índice reajustado, em percentual.
'''

sal = float(input())
p = "%"

if sal <= 400:
	pc = 15
elif 400 < sal <= 800:
	pc = 12
elif 800 < sal <= 1200: 
	pc = 10
elif 1200 < sal <= 2000: 
	pc = 7
else: 
	pc = 4


print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %d %s" %((sal + (sal * pc / 100)), (sal * pc / 100), pc, p))