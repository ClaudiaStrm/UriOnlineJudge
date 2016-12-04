'''
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser 
no mês de Abril, iniciando e terminando dentro do mês. O problema é que 
Pedrinho quer calcular o tempo em segundos que o evento vai durar, uma vez 
que ele sabe quando inicia e quando termina o evento..

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá 
ajudar Pedrinho a calcular a duração deste evento.
'''

s1, inDia = input().split()
inHora, inMin, inSeg = input().split(':')
s2, fimDia = input().split()
fimHora, fimMin, fimSeg = input().split(':')

i = 0
for x in range (int(inDia), int(fimDia)):
	i += 1
seg = i * 24 * 60 * 60

inHora = int(inHora) * 60 * 60
inMin = int(inMin) * 60
inMenos = inHora + inMin + int(inSeg)

fimHora = int(fimHora) * 60 * 60
fimMin = int(fimMin) * 60
fimMais = fimHora +fimMin + int(fimSeg)

segTotal = seg + fimMais - inMenos

hora = segTotal / 3600
dia = hora / 24
hora = hora % 24
minu = (segTotal % 3600) / 60
seg = (segTotal % 60)
print("%d dia(s)\n%d hora(s)\n%d minuto(s)\n%d segundo(s)" %(dia, hora, minu, seg))
