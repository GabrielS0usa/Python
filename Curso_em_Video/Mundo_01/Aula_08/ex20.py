# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o nome
# dos quatro alunos e mostre a ordem sorteada.

from random import shuffle as ord

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

alu = [a1, a2, a3, a4]

ord(alu)

print(f'A ordem de apresentação é {alu} .')



