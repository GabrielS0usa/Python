#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
nome = str(input('Digite o nome da sua cidade: ')).strip(' ').title()
# nome_div = nome.split()
# santo = 'Santo' in nome_div[0]
# print(f'Essa cidade começa com "Santo" {santo}')
print('Essa cidade começa com "Santo":', nome.startswith('Santo'))
print(nome[:5] == 'Santo')
