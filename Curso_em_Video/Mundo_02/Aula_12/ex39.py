'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

nome = str(input('Olá! Qual o seu nome? ')).title()
sexo = int(input('''Qual seu sexo:
1- Homem
2- Mulher
Opção: '''))
if sexo == 1:
    nac = int(input(f'Em que ano você nasceu {nome}? '))
    ano = date.today().year
    idade = ano - nac
    if idade < 18:
        print(f'{nome} você tem {idade} anos em {ano} e você ainda vai se alistar.')
        print(f'Falta {18 - idade} anos.')
        print(f'Seu alisamento vai ser em {ano+(18-idade)}.')
    elif idade == 18:
        print(f'{nome} você tem {idade} anos em {ano} e está na hora de se alistar.')
    elif idade > 18:
        print(f'{nome} você tem {idade} anos em {ano} e já passou do tempo de alistamento a {idade - 18} anos.')
        print(f'Seu alisamento foi em {ano-(idade-18)}.')
elif sexo == 2:
    print('Você não precisa se alistar.')
else:
    print('Opção invalida.')