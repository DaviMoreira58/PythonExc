# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
# valor que estão na tupla.

"""from random import randint
n0 = randint(0,10)
n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
numeros = (n0, n1, n2, n3, n4)
print(f'Os valores sorteados foram: {numeros}')
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')""" # Meu jeito

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
    randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
