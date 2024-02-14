# math = blibioteca de matematica
#     ceil = Faz um arredondamento para cima
#     floor = Floor faz um arredondamento para baixo
#     trunc = Vai trunca um número, vai eliminar da virgula para frente
#     pow = Potencia
#     sqrt = Raiz quadrada
#     factorial = Faz calculos fatorial
# import math = Importa toda a blibioteca de math
# from math import ... = Importa apenas a função desejada. Colocando uma virgula pode importa mais de uma desejada
# import + espaço + ctrl = a lista de importação
# ------------------------------------------------------------------------------------------------------------------------
# RANDOM
# 1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa
# 2. Você quer fazer um sorteio entre 300 nomes em uma lista de nomes
# 3. Você quer escolher aleatóriamente um número de 10-100
# 5. Você quer nomes de usuário aleatóriamente
# 6. Você quer gerar senhas seguras

# ----------------------------------------------------------------------------------------------------------------------
# from math import sqrt, floor
#
# num = int(input('Digite um número: '))
# raiz = sqrt(num)
# print(f'A raiz de {num} é igual a {floor(raiz)} .')
#
import random
#
# num = random.randint(1, 10)
#
# print(num)

# import emoji
# print(emoji.emojize("Olá, Mundo! :earth_americas:", language='alias'))

print(random.random()) # Valor de 0.0 até 1.0
print(random.uniform(4, 10)) # Valor decimal do mínimo ao máximo, entre os valores dentro dos parentes
print(random.randint(12, 55)) # Valor inteiro do mínimoo ao máximo, entre os valores dentro dos parentes

cores = ['verde', 'Vermelho', 'azul']
print(random.choice(cores)) # Escolhe uma opção dentro de uma fonte

cartas_de_um_baralho = ['carta1', 'carta2', 'carta3', 'carta4', 'carta5']
random.shuffle(cartas_de_um_baralho)
print(cartas_de_um_baralho)



