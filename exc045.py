# Faça um programa que faça o computador jogar jokenpo com você

'''from random import randint
from time import sleep
print('\033[4;36mTENTE VENCER O COMPUTADOR NO JOKENPO\033[m')
jogador = int(input(\033[1;31mFaça a sua escolha\033[m
\033[1;35m[ 1 ] PEDRA\033[m
\033[1;36m[ 2 ] PAPEL\033[m
\033[1;37m[ 3 ] TESOURA\033[m ))
pc = randint(1, 3)
print('\033[32mVEZ DO COMPUTADOR ESCOLHER!\033[m')
sleep(1)
print('\033[1mProcessando...\033[m')
sleep(3)
if jogador == 1 and pc == 1 or jogador == 2 and pc == 2 or jogador == 3 and pc == 3:
    print('O Jogador Escolheu {} e o computador {}, por isso deu Empate'.format(jogador, pc))
if jogador == 1 and pc == 3 or jogador == 2 and pc == 1 or jogador == 3 and pc == 2:
    print('Jogador Venceu, o computador escolheu {}'.format(pc))
if pc == 1 and jogador == 3 or pc == 2 and jogador == 1 or pc == 3 and jogador == 2:
    print('O computador venceu, o jogador escolheu {}'.format(jogador))'''

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
