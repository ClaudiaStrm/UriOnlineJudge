
'''
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números 
impares entre eles.
'''

a = int(input())
b = int(input())
i = 0

if b < a:
	for x in range((a-1), b, -1):
		print(x)
		if x % 2 != 0:
			i = i + x
else:
	for x in range((a+1), b):
		print(x)
		if x % 2 != 0:
			i = i + x
print(i)
