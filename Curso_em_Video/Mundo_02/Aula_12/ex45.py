from random import choice as sor
import emoji
from time import sleep
print('-=-' * 20)
print(emoji.emojize('Vamos jogar jokenpô 👊✋✌️', language='alias'))
sleep(1.5)
opw = 1
while opw == 1:
    print('Escolha uma opção')
    op = int(input(emoji.emojize('''
1- Pedra 👊
2- Papel ✋
3- Tesoura ✌️
Opção: ''', language='alias')))
    print('Processando...')
    sleep(1)
    if op == 1:
        op = 'Pedra 👊'
    elif op == 2:
        op = 'Papel ✋'
    elif op == 3:
        op = 'Tesoura ✌️'
    else:
        print('Opção invalida')
        exit(op != 1)

    opção =['Pedra 👊', 'Papel ✋', 'Tesoura ✌️']
    pc = sor(opção)
    print('-=-' * 20)
    if op == pc:
        print('Empate')
    elif op == 'Pedra 👊' and pc == 'Tesoura ✌️' or op == 'Papel ✋' and pc == 'Pedra 👊' or op == 'Tesoura ✌️' and pc == 'Papel ✋':
        print('Você ganhou')
    elif pc == 'Pedra 👊' and op == 'Tesoura ✌️' or pc == 'Papel ✋' and op == 'Pedra 👊' or pc == 'Tesoura ✌️' and op == 'Papel ✋':
        print('Você perdeu')
    print(emoji.emojize(F'Você jogou {op} e o pc jogou {pc}', language='alias'))
    print(' ')
    opw = int(input('''Opções
    1- jorgar novamente
    2- Encerrar
    opção: '''))

# op = int(input('''Escolha uma opção
# 1- Par
# 2- Impar
# Opção: '''))
#
# if op == 1:
#     op = 'Par'
#     pc = 'Impar'
# elif op == 2:
#     op = 'Impar'
#     pc = 'Par'
# else:
#     print('Opção invalida')
#     exit(op != 1)
# n1 = int(input('Digite um número de (0/10): '))
# n2 = random.randint(0, 10)
# print(' ')
# print('-=-' * 20)
# print(' ')
# resutado = (n1 + n2) % 2
#
# print(f'Você escolheu {op} e jogou {n1}.')
# print(f'O computador ficou com {pc} e jogou {n2}.')
# print('Total:', n1 + n2)
# if resutado == 0:
#     print(f'{n1+n2} é Par')
#     if op == 'Par':
#         print('\033[32mVocê ganhou e o computador perdeu!\033[m')
#     else:
#         print('\033[31mVocê perdeu e o computador ganhou!\033[m')
# elif resutado != 0:
#     print(f'{n1+n2} é Impar')
#     if op == 'Impar':
#         print('\033[32mVocê ganhou e o computador perdeu!\033[m')
#     else:
#         print('\033[31mVocê pedeu e o computador ganhou!\033[m')

