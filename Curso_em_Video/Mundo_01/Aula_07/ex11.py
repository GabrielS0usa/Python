larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = larg * alt
tinta = area / 2
print(f'Sua parede tem a dimensão de {larg}x{alt}m² e a sua área é de {area}m².')
print(f'Para pintar esse parede, você precisará de {tinta}l de tinta.')
