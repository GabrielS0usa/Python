# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    if r1 == r2 and r2 == r3:
        print('As retas formam um triâgulo equilátero')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('As retas formam um triâgulo Isósceles')
    elif r1 != r2 != r3 != r1:
        print('As retas formam um triângulo Escaleno')
else:
    print('As retas não formam um triângulo.')