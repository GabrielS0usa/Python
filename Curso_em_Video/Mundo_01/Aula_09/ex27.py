#Faça um programa que leia o nome de uma pessoa , mostre em seguida o primeiro nome e o último nome separadamente.
n = str(input('Digite o seu nome completo: ')).strip().title()
nome = n.split()
print(f'Muito prazer wm te conhecer {n}!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')
