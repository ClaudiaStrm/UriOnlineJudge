'''
Neste problema, você deverá ler 3 palavras que definem o tipo de animal 
possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida 
conclua qual dos animais seguintes foi escolhido, através das três palavras 
fornecidas.
'''

pal1 = input()
pal2 = input()
pal3 = input()

if pal1 == 'vertebrado':
	if pal2 == 'ave' and pal3 == 'carnivoro':
		print("aguia")
	elif pal2 == 'ave' and pal3 == 'onivoro':
		print("pomba")
	elif pal2 == 'mamifero' and pal3 == 'onivoro':
		print("homem")
	else:
		print("vaca")

else:
	if pal2 == 'inseto' and pal3 == 'hematofago':
		print("pulga")
	elif pal2 == 'inseto' and pal3 == 'herbivoro':
		print("lagarta")
	elif pal2 == 'anelideo' and pal3 == 'onivoro':
		print("minhoca")
	else:
		print("sanguessuga")