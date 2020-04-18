# Crie um programa que tenha uma tupla com varias palavras(não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
# Na palavra APRENDER temos a e e

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programardor', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
x = 0
for cont in range(0, len(palavras)):
    print(f'{palavras[x]}')
    x += 1

