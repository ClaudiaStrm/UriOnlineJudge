'''
Leonardo Viana é um garoto fascinado por jogos de tabuleiro. Nas férias de janeiro, ele aprendeu um jogo chamado "Campo minado", que é 
jogado em um tabuleiro comN células dispostas na horizontal. O objetivo desse jogo é determinar, para cada célula do tabuleiro, o número 
de minas explosivas nos arredores da mesma (que são a própria célula e as células imediatamente vizinhas à direita e à esquerda, caso 
essas existam). Por exemplo, a figura abaixo ilustra uma possível configuração de um tabuleiro com 5 células:



A primeira célula não possui nenhuma mina explosiva, mas é vizinha de uma célula que possui uma mina explosiva. Nos arredores da segunda 
célula temos duas minas, e o mesmo acontece para a terceira e quarta células; a quinta célula só tem uma mina explosiva em seus 
arredores. A próxima figura ilustra a resposta para esse caso.



Leonardo sabe que você participa da OBI e resolveu lhe pedir para escrever um programa de computador que, dado um tabuleiro, imprima o 
número de minas na vizinhança de cada posição. Assim, ele poderá conferir as centenas de tabuleiros que resolveu durante as férias.
'''

a = int(input())
mina = []
b = 0
lista = []
for x in range(0, a):
	x = int(input())
	mina.append(x)
if a == 1:
	print(mina[0])
else:
	b = mina[0] + mina[1]
	print(b)

	for x in range(1, (a-1)):
		b = 0
		b = mina[x-1] + mina[x] + mina[x+1]
		print(b)

	b = mina[a-1] + mina[a-2]
	print(b)
