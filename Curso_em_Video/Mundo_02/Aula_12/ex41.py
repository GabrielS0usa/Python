# A Confederação Nacional de Nataçãoprecisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRI
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date
atual = date.today().year
nac = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - nac
print(f'O atleta tem {idade}.')
if idade <= 9:
    print('É um atleta mirim')
elif idade > 9 and idade <= 14:
    print('É um atleta infantil')
elif idade > 14 and idade <= 19:
    print('É um atleta junior')
elif idade > 19 and idade <= 25:
    print('É um atleta sênior')
else:
    print('É um atleta master')