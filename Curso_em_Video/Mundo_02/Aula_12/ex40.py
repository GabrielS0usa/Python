# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

print('Vamos calcular a sua média de notas.')
nome = str(input('Qual é o seu nome? ')).title()
n1 = float(input('Digite a nota n1: '))
n2 = float(input('Digite a nota n2: '))
med = (n1 + n2) / 2
if med < 5.0:
    print(f'{nome} você tirou {med:.1f} está reprovado!')
elif med >= 5.0 and med <= 6.9:
    print(f'{nome} você tirou {med:.1f} está de recuperação!')
elif med >= 7.0:
    print(f'{nome} voc ê tirou {med:.1f} está aprovado!')