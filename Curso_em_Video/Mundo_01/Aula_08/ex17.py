# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de triângulo retângulo, calcule e mostre
# o comprimento da hipotenusa.

from math import pow, sqrt, hypot

ad = float(input('Digite o valor do cateto adjacente do triângulo: '))
op = float(input('Digite o valor do cateto oposto do triângulo: '))
# pot = (pow(ad, 2) + pow(op, 2))
# hip = sqrt(pot)
hip = hypot(ad, op)
print(f'A hipotenusa do cateto adjacente {ad} e cateto oposto {op}, e a hipotenusa é {hip:.2f}')

