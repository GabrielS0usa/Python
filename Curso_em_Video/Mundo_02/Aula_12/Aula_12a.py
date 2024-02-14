# Essa é uma condição alinhada.
nome = str(input('Qual é o seu nome ? '))
if nome == 'Gabriel':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Christopher' or nome == 'Mariana':
    print('Seu nome é bem normal no Brasil.')
elif nome in 'Ana Clúdia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Que nome normal!')
print(f'Tenha um bom dia, {nome}')