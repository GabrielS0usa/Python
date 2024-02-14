'''Escrava um programa que pergunte o salário de um Funcionário e calcule o valor do salário mais o aumento.
Para salários superiores a R$1.25O,OO calcula um aumento de 10%. Para os inferiores ou iguais, o aumanto é de 15%.'''

sal = float(input('Digite o valor do seu salário: '))
if sal <= 1250:
    poc = sal * 15 / 100
    print(f'Seu salário de R${sal} com o aumento de 15% ficou R${sal + poc :.2f} ')
else:
    poc = sal * 10 / 100
    print(f'Seu salário de R${sal} com o aumento de 10% ficou R${sal + poc :.2f} ')
