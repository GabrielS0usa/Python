# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
# Digite um número real: 6.127
# O número 6.127 tem a parte inteira 6.

from math import trunc

'''num = float(input('Digite um número real: '))
inte = num.__trunc__()
inte = trunc(num)
print(f'O número {num} tem a parte inteira {inte} .')'''

num = float(input('Digite um número real: '))
print(f'O valor digitado é foi {num} e sua porção inteira é {int(num)} .')

