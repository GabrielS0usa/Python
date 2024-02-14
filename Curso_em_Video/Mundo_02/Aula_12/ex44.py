# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print(f'{" LOJAS GABRIEL ":=^40}')
produto = float(input('Digite o valor do produto: R$'))
print('-=- Selecione a forma de pagamento -=-')
print('''
1- À vista
2- À vista no cartão
3- 2x no cartão
4- 3x ou mais no cartão''')
print('-=-' * 20)
forma = int(input('Selecione uma opção de 1 a 4: '))
if forma == 1:
    desconto = produto * 10 / 100
    print(f'Com pagamento à vista fica R${produto - desconto:.2f} .')
elif forma == 2:
    desconto = produto * 5 / 100
    print(f'Com pagamento à vista no cartão fica R${produto - desconto:.2f} .')
elif forma == 3:
    print(f'Com o pagamento em 2x sem juros fica duas parcelas de R${produto / 2 :.2f} .')
elif forma == 4:
    vezes = int(input('Quantas vezes deseja dividir: '))
    juros = produto * 20 / 100
    prec = produto + juros
    print(f'Com o pagamento em {vezes}x ou mais vezes fica R${prec:.2f} em {vezes}x de R${prec / vezes:.2f} ')
else:
    print('\033[31mOpção invalida.\033[m')