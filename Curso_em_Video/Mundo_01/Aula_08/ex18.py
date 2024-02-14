# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan

angulo = int(input('Digite o valor de um ângulo :'))
cv = radians(angulo) # Converte o ângulo x de graus para radianos.
seno = sin(cv) #Retorna o seno de x radianos.
print(f'O ângulo de {angulo}° tem o SENO de {seno:.2f}')
cosseno = cos(cv) #Retorna o cosseno de x radianos.
print(f'O ângulo de {angulo}° tem o COSSENO de {cosseno:.2f}')
tangente = tan(cv) #Retorna o tangente de x radianos.
print(f'O ângulo de {angulo}° tem a TANGENTE de {tangente:.2f}')



