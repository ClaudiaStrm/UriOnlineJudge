'''
Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
1 x N = N      2 x N = 2N        ...       10 x N = 10N
'''

a = int(input())

for x in range(1,11):
	print("%d x %d = %d" %(x, a, x * a))