'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os 
valores em ordem crescente, uma linha em branco e em seguida, os valores na 
sequência como foram lidos.
'''

a = [int(x) for x in input().split()]
n1, n2, n3 = a[0], a[1], a[2]

a.sort()
for x in a:
	print(x)

print("\n%d\n%d\n%d" %(n1, n2, n3))