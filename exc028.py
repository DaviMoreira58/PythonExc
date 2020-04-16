# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
# e peça para o usuario tentar descobrir qual foi u numero escoljido pelo computador ,
# o programa devera escrever na tela se o usuario venceu ou perdeu
'''
import random

n = int(input('Qual o numero? '))
r = random.randint(0, 5)
if n == r:
    print('Acertou mizeravi!')
else:
    print('errooooou!!')
print(r)'''

from random import randint
from time import sleep
computador = randint(0, 5)
print('\033[31m-=-\033[m' * 20)
print('Vou pensar em um numero de 0 a 5. Tente adivinhar...')
print('\033[31m-=-\033[m' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('\033[32mProcessando...\033[m')
sleep(2)
if jogador == computador:
    print('\033[35;1mParabens! Voce conseguiu me vencer!\033[m')
else:
    print('\033[4;35mGanhei! Eu pensei no numero {} e não no {}\033[m'.format(computador, jogador))