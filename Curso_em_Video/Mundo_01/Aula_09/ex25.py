#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = str(input('Digite seu nome completo: ')).strip(' ')
# silva = 'Silva' in nome
print(f'Esse nome tem "Silva": {"Silva" in nome.title()}')