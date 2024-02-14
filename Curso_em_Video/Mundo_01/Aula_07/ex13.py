'''sala = float(input('Digite o seu salário para ver o valor do aumento:'))
poc = sala * 15 / 100
novo = sala + poc
print(f'O seu salário subiu de {sala:.2f} para {novo:.2f}.')'''

preco = float(input('Digite o valor da compra: R$'))
avista = preco - (preco * 8 / 100)
parc = preco - (preco * 5 / 100)

print(f'O valor da compra é R${preco:.2f} com o desconto de 8% de pagamento avista fica R${avista:.2f}, e '
      f'parcelado com o desconto de 5% fica R${parc:.2f} .')
