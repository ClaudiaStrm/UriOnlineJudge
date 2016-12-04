#-*- coding:utf-8 -*-
'''
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. 
Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
Perimetro = XX.X
Em caso negativo, calcule a área do trapézio que tem A e B como base e C como 
altura, mostrando a mensagem
Area = XX.X
'''
a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

if ((b - c) < a < (b + c)) & ((a - c) < b < (a + c)) & ((a - b) < c < (a + b)) == True:
	print('Perimetro = %.1f' %(a + b + c))
else:
	print('Area = %.1f' %(c * (a + b) / 2))