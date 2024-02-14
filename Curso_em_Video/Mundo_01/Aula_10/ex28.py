'''Escreva um programa que faça o computador "pensar" um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.'''
#O progrma deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint as sor
import emoji
from time import sleep

sorteio = sor(0,5)
print(f'\033[1;32m-=-\033[m' * 22)
print(emoji.emojize('\033[7m:bow: Estou pensando em um número entre 0 e 5. Tente adivinhar...    \033[m', language='alias'))
print('\033[1;32m-=-\033[m' * 22)
usu = int(input('\033[1;33mEm que número eu pensei ? \033[m'))
print('\033[35mPROCESSANDO...\033[m')
sleep(2)
if usu == sorteio:
    print(f'\033[32mVocê ganhou! É o número {sorteio}\033[m')
else:
    print('\033[31mVocê perdeu!\033[m')
    print(f'\033[31mEu pensei no número {sorteio} e não no {usu}\033[m')
