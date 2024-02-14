'''Escrava um programa que leia a valocidade de um carro.
Sa ela ultrapassar 80Hk/h, mostra uma mansagam dizendo que ela Foi multado.
A multa vai custar R$7,OO por cada km acima do limite.'''

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'}

vel = int(input(f'{cores["amarelo"]}Digite uma velocidade: {cores["limpa"]}'))
if vel>80:
    print(f'{cores["amarelo"]}Você ultrapassou {vel - 80}Km/h da velocidade permitida que é 80Km/h{cores["limpa"]}')
    print(f'{cores["vermelho"]}A multa é de R${(vel - 80) * 7:.2f}{cores["limpa"]}')
else:
    print(f'{cores["verde"]}Tenha um bom dia! Dirija com segurança!{cores["limpa"]}')