from random import choice

nome = str(input('Digite seu nome: '))
nomes = ['Gabriel', 'Pedro', 'Vitor', 'Maria', 'Paula', 'Ana']
print(f'Olá {nome}!'.replace(nome, choice(nomes)))