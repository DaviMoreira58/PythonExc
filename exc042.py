# Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo
# de triangulo será formado:
# Equilátero: Todos os lados iguais
# Isóceles: dois lados iguais
# Escaleno: Todos os lados diferentes

'''r1 =float(input('Primeiro segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'amarelo':'\033[1;33m',
         'vermelho':'\033[1;31m'}
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('{}Pode ser formado um triangulo{}'.format(cores['amarelo'], cores['limpa']))
    if r1 == r2 == r3:
        print('{}E o Triangulo será equilatero{}'.format(cores['azul'], cores['limpa']))
    if r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('{}E o Triangulo será isóceles{}'.format(cores['azul'], cores['limpa']))
    if r1 != r2 and r2 != r3 and r3 != r1:
        print('{}E o Triangulo será escaleno{}'.format(cores['azul'], cores['limpa']))
else:
    print('{}Não pode ser formado um triangulo{}'.format(cores['vermelho'], cores['limpa']))'''

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triangulos!')

