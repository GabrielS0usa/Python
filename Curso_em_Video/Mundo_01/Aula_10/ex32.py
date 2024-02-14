'''Faça um programa que leia um ano e mostre se ele é BISSEXTO'''
from datetime import date
ano = int(input('Digite um ano para saber se é BISSEXTO: Coloque 0 para analisar o ano atual: '))
'''if ano.endswith('00') == True:
    inte1 = int(ano)
    if inte1 % 400 == 0:
        print(f'O ano de {ano} foi um ano bissexto')
    else:
        print(f'O ano de {ano} não foi um ano bissexto')
else:
    inte2 = int(ano)
    if inte2 % 4 == 0:
        print(f'O ano de {ano} foi um ano bissexto')
    else:
        print(f'O ano de {ano} não foi um ano bissexto')
'''
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')