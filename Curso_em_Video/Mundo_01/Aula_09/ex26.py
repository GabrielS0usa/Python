#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip(' ')
print(f'A letra "a" aparece {frase.lower().count("a")}° vezes na frase: {frase}.')
# print(frase.lower().index("a")+1)
# print(frase.lower().rindex("a")+1)
print(f'''A letra "a" Aprece a primeira vez na {frase.lower().find("a") + 1}° posição.
E aparece a ultima vez na {frase.lower().rfind("a")+1}° posição.''')