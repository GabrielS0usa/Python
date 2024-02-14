
# capitalize() Converte o primeiro caractere em maiúscula
# casefold() Converte string em minúsculas
# center() Retorna uma string centralizada
# count()Retorna o número de vezes que um valor especificado ocorre em uma string
# encode()Retorna uma versão codificada da string
# endswith()Retorna verdadeiro se a string terminar com o valor especificado
# expandtabs()Define o tamanho da tabulação da string
# find() Procura na string por um valor especificado e retorna a posição de onde foi encontrado
# format() Formata valores especificados em uma string
# format_map() Formata os valores especificados em uma string
# index() Pesquisa a string por um valor especificado e retorna a posição de onde foi encontrado
# isalnum() Retorna True se todos os caracteres na string forem alfanuméricos
# isalpha() Retorna True se todos os caracteres da string estiverem no alfabeto
# isascii() Retorna True se todos os caracteres na string forem caracteres ASCII
# isdecimal() Retorna True se todos os caracteres na string forem decimais
# isdigit() Retorna True se todos os caracteres na string forem dígitos
# isidentifier() Retorna True se a string for um identificador
# islower() Retorna True se todos os caracteres da string forem minúsculos
# isnumeric() Retorna True se todos os caracteres na string forem numéricos
# isprintable() Retorna True se todos os caracteres na string forem imprimíveis
# isspace() Retorna True se todos os caracteres na string forem espaços em branco
# istitle() Retorna True se a string seguir as regras de um título
# isupper() Retorna True se todos os caracteres da string forem maiúsculos
# join () Converte os elementos de um iterável em uma string
# ljust() Retorna uma versão justificada à esquerda da string
# lower() Converte uma string em letras minúsculas
# lstrip () Retorna uma versão de corte à esquerda da string
# maketrans() Retorna uma tabela de tradução para ser usada nas traduções
# partition() Retorna uma tupla onde a string é dividida em três partes
# replace() Retorna uma string onde um valor especificado é substituído por um valor especificado
# rfind() Procura na string por um valor especificado e retorna a última posição de onde foi encontrado
# rindex() Procura na string um valor especificado e retorna a última posição de onde foi encontrado
# rjust() Retorna uma versão justificada à direita da string
# rpartition() Retorna uma tupla onde a string é dividida em três partes
# rsplit() Divide a string no separador especificado e retorna uma lista
# rstrip() Retorna uma versão de corte à direita da string
# split () Divide a string no separador especificado e retorna uma lista
# splitlines() Divide a string nas quebras de linha e retorna uma lista
# startswith() Retorna verdadeiro se a string começar com o valor especificado
# strip() Retorna uma versão aparada da string
# swapcase() Troca as letras maiúsculas e minúsculas e vice-versa
# title() Converte o primeiro caractere de cada palavra para maiúscula
# translate () Retorna uma string traduzida
# upper() Converte uma string em letras maiúsculas
# zfill () Preenche a string com um número especificado de valores 0 no início

frase = 'Curso em Video Python'
print(frase[3]) # Mostra a letra do valor determinado.
print(frase[3:13]) # Mostra da do valor determinado até o valor determinado depois dos dois pontos.

print(frase[::]) # Mostra do inicio ao fim.

print((f'''Sempre amei teu lado passional
Como equilibrava o racional
Comigo nos braços ou com parafal
Aquele você nem você é igual
Eu também mudei, eu não sei qual foi
Eu me acomodei, fingi ser normal
Tu entrar em casa sem dizer "oi"
Talvez eu também vá sem dizer tchau
Ao se aproximar eu me apaixonei
Ao se abandonar eu me descuidei
Que bandido é esse que pode tudo?
E que favela é essa que não tem lei?
Neurose de novinha não é meu forte
Não aguenta o plantão então larga o porte
Sei meu valor só que tu, parece
Que às vezes esquece ou não merece
Se eu soubesse que a vida seria assim
Não escolheria essa aqui pra mim
Mas quantos caminhos foram confundidos
Desde o nosso início pra encontrar o fim?''')) # Mostra o texto com a formatação original sem precisar da print por print.