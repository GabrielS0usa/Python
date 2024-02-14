'''Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.'''

km = float(input('Digite a distância em km da viagem: '))
if km <=200:
    print(f'O valor da viagem de {km:.2f}km é R${km * 0.50 :.2f}.')
else:
    print(f'O valor da viagem de {km:.2f}km é R${km * 0.45 :.2f}.')