pre = float(input('Digite um preço para ver o valor atual: R$'))
poc = pre * 5 / 100
novo = pre - poc
print(f'O produto que custava R${pre:.2f} com de desconto de 5% ficou R${novo:.2f} .')