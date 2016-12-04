'''
Leia um número inteiro que representa um código de DDD para discagem 
interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando 
a tabela abaixo:
Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o 
programa deverá informar:
DDD nao cadastrado
'''

a = int(input())
DDD = [61, 71, 11, 21, 32, 19, 27, 31]
cidade = ['Brasilia', 'Salvador', 'Sao Paulo','Rio de Janeiro', 'Juiz de Fora',  'Campinas', 'Vitoria', 'Belo Horizote']
i = 0
for x in DDD:
	if DDD[i] == a:
		print(cidade[i])
	i += 1	
if a not in DDD:
	print('DDD nao cadastrado')