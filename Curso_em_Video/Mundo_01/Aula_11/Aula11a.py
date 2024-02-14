print('\033[33;44m Olá, Mundo!\033[m')

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7m'}

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