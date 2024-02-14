'''
+ = Adição                  == Significa resutado da soma
- = Subtração               = Significa reseber
* = Multiplicação           ---------------------
/ = Divisão                 Ordem de precedência:
** = Potência               Parênteses;
// = Divisão Inteira        Expoentes;
% = Resto da Divisão        Multiplicações e divisões; (da esquerda para a direita);
                            Somas e subtrações. (da esquerda para a direita);
Alt + 3 = ♥♥♥♥
'''

'''print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 ** 2)
print(5 // 2)
print(5 % 2)
print(5 + 3 * 2)
print(3 * 5 + 4 ** 2)
print(3 * (5 + 2) ** 2)

nome = input('Qual o seu nome ?')
print(f'Prazer em te conhecer {nome}!')

nome = input('Qual o seu nome ?')
print(f'Prazer em te conhecer !{nome:♥<20}!')'''

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
re = n1 % n2
e = n1 ** n2
print(f'A soma é {s}, o produto é {m}, a divisão é {d:.3f}, a divisão inteira é {di}, o resto da divisão é {re}, a exponenciação é {e}.')

print(f'A soma é {s}, o produto é {m}, a divisão é {d:.3f}, a '
      f'divisão inteira é {di}, o resto da divisão é {re}, a exponenciação é {e}.')

print(f'A soma é {s}, o produto é {m}, a divisão é {d:.3f}', end=' ')
print(f'divisão inteira é {di}, o resto da divisão é {re}, a exponenciação é {e}.')

print(f'A soma é {s}, o produto é {m}, a divisão é {d:.3f}')
print(f'divisão inteira é {di}, o resto da divisão é {re}, a exponenciação é {e}.')


