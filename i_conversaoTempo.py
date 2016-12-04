'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado 
evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.
'''
tempo = int(input())
hora = tempo / 3600
minu = (tempo % 3600) / 60
seg = (tempo % 60)
print("%d:%d:%d" %(hora, minu, seg))
