'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A 
seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
'''

a = [int(x) for x in input().split()]

if (a[0] == a[2]) and (a[1] > a[3]):
	t = 23
elif a[0] == a[2] and a[1] < a[3]:
	t = 0
elif (a[0] < a[2]) and (a[1] > a[3]):
	t = 0
elif a[0] > a[2] and a[1] > a[3]:
	t = 24 - a[0] + a[2] - 1
elif a[0] == a[2] and a[1] == a[3]:
	t = 24
	
elif a[0] < a[2]:
	t = a[2] - a[0]
elif a[0] > a[2]:
	t = 24 - a[0] + a[2]

if a[1] == a[3]:
	m = 0
elif a[1] < a[3]:
	m = a[3] - a[1]
else:
	m = 60 - a[1] + a[3]

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(t, m))