# Escreva um programa em Python que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

x = int(input('Entre com um valor: '))
c = int(input('''
- 1 para binário
- 2 para octal
- 3 para hexadecimal: '''))
print(' ')
print('-=-' * 20)
print(' ')
if c == 1:
    bina = bin(x)
    print(f'({x}) decimais em binário é ({bina[2:]})')
elif c == 2:
    octa = oct(x)
    print(f'({x}) decimais em octal é ({octa[2:]})')
elif c == 3:
    hexa = hex(x)
    print(f'({x}) decimais em hexadecimal é ({hexa[2:]})')
else:
    print('Opção invalida!')