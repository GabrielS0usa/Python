dia = int(input('Quantos dias de aluguel ?'))
km = int(input('Quantos km percorridos ?'))
alu = dia * 60
dist = km * 0.15
print(f'O preço de {dia} dias de aluguel fica R${alu:.2f} .')
print(f'O preço de {km}km percorridos fica R${dist:.2f} .')
print(f'Totalizando R${dist + alu:.2f} .')
