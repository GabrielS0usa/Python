# FATIAMENTO
# Quando se trabalha com fatiamento ou ranger, sempre levamos em consideração o ultimo número + 1, porque ele sempre exclui o ultimo.

frase = 'Curso em Video Python'
print('Linha-5', frase[9:21:2])# pula de 2 em dois.
print('Linha-6', frase[:5])# Até o número determinado.
print('Linha-7', frase[5:])# Do número determinado até o fim.
print('Linha-8', frase[9::3])#Do número determinado até o fim pulando de 3 em 3.

#ANÁLISE

print('Linha-12', len(frase)) # Análisa o tamanho da frase.
print('Linha-13', frase.count('o')) # Conta quantas vezes aparece o caractere entre parenteses.
print('Linha-14', frase.count('o',0,13)) # Conta quantas vezes aparece o caractere entre parenteses do número determinado até o o outro valor determinado.
print('Linha-15', frase.find('deo')) # Mostra quando começou a frase entre parenteses.
print('Linha-16', frase.find('android')) # Retorna o valor -1, sinal que a frase não foi encontrada.
print('Linha-17', 'Curso' in frase) # Existe a palavra entre aspas.

#TRASFORMAÇÃO

print('Linha-21', frase.replace('python', 'android')) # Substitui a palavra por outra entre parenteses.
print('Linha-22', frase.upper()) # Deixa a frase em maiusculo.
print('Linha-23', frase.lower()) # Deixa a frase em minusculo.
print('Linha-24', frase.capitalize()) # Deixa apenas a primeira letra da frase em maiusculo e o resto em minuscula.
print('Linha-25', frase.title()) # Deixa todas as palavras da frase com a primeira letra em maiusculas.

frase2 = '   Aprenda Python  '
print('Linha-28', frase2)

print('Linha-30', frase2.strip()) # Remove todos os espaços inuteis na frente e no final da frase.
print('Linha-31', frase2.rstrip()) # Remove todos os espaços inuteis na direita da frase no caso o final da frase.
print('Linha-32', frase2.lstrip()) # Remove todos os espaços inuteis na esquerda da frase no caso o início da frase.

#Divisão

# Estudar split e strip.

print('Linha-38', frase.split()) # Faz uma divisão onde tem espaço na frase.

frase3 = frase.split() # Aqui eu coloquei a frase 1 em split "Divisão da palavra das frases" em outra variavel.

print('Linha-42', '-'.join(frase3)) # Junta as palavras colocando um separador de acordo com o que está em aspas.

print('Linha-44', frase3 [3] [3]) # Mostra a posição da frase dividida, mas a posição da letra de acordo com o valor informado.


