'''
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do 
jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo 
uma duração mínima de 1 hora e máxima de 24 horas.
'''

a = [int(x) for x in input().split()]

if a[0] == a[1]:
	t = 24
elif a[0] < a[1]:
	t = a[1] - a[0]
else:
	t = 24 - a[0] + a[1]
print("O JOGO DUROU %d HORA(S)" %t)
