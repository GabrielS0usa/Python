# Um professor quer sortear um dos seus alunos apara apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e
# escrevendo o nome do escolhido.
from random import choice

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

alu = [a1, a2, a3, a4]

sor = choice(alu)

print(f'O aluno sorteado para apagar o quadro foi {sor} .')
