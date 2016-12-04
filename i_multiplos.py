'''
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem
"Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são
múltiplos entre si.
'''

a = [int(x) for x in input().split()]
a.sort()

if a[1] % a[0] == 0:
	print('Sao Multiplos')
else:
	print("Nao sao Multiplos")