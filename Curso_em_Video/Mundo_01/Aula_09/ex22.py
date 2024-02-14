#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras tem (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()
print(f'''Nome com todas as letras maiúsculas {nome.upper()}.
Nome com todas as letras minúsculas {nome.lower()}.
Quantas letras tem o nome: {len(''.join(separado))}.
Quantas letras tem primeiro nome:  {len(separado [0])}.''')
