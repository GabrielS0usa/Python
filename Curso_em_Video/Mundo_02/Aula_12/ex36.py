# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('Bem-Vindo simulador de financiamento de imovel')
nome = str(input('Qual é o seu nome ? ')).title()
print('1° Primeiro')
ca = float(input('Digite o valor da casa: R$'))
print('2° Segundo')
sa = float(input('Digite o valor do seu salário: R$'))
print('3° Terceiro')
anos = int(input('Digite em quantos anos deseja financiar o imovel: '))
casa = ca * 1000
sala = sa * 1000
parc = casa / (anos * 12)
p30 = sala * 30 / 100
print(" ")
print('-=-' * 60)
print(" ")
if p30 >= parc:
    print(f'Seu financiamento da casa no valor de R${casa.__trunc__()} foi aprovado Sr.{nome}.')
    print(f'O valor da parcela é de R${parc.__trunc__():.2f} em {anos * 12} meses por {anos} anos')
else:
    print(f'Sr.{nome} o financiamento da casa de R${casa.__trunc__()} foi negado, poque o valor da parcela de R${parc:.2f}'
          f' ultrapassou os 30% do seu salario de R${sala :.2f} que representa {p30.__trunc__():.2f} .')