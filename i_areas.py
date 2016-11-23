'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre: 
a) a área do triângulo retângulo que tem A por base e C por altura. 
b) a área do círculo de raio C. (pi = 3.14159) 
c) a área do trapézio que tem A e B por bases e C por altura. 
d) a área do quadrado que tem lado B. 
e) a área do retângulo que tem lados A e B. 
'''

val = [float(x) for x in input().split()]
a = val[0]
b = val[1]
c = val[2]

print('TRIANGULO: %.3f' %((a * c) / 2))
print('CIRCULO: %.3f' %(3.14159 * c**2))
print('TRAPEZIO: %.3f' %(c * (a + b) / 2))
print('QUADRADO: %.3f' %(b**2))
print('RETANGULO: %.3f' %(a * b))
