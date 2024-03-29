# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10
# só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessarios para vencer

'''from random import randint
pc = randint(0, 10)
jogador = int(input('Qual é o seu palpite? '))
soma = 0
while jogador != pc:
    soma += 1
    input('Tente de novo')
    print(pc)
    if pc > jogador:
        print('Mais')
    if pc < jogador:
        print('Menos')
print('Acabou')'''

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez. ')
        elif jogador > computador:
            print('Menos... Tente mais uma vez. ')
print('Acertou com {} tentativas!'.format(palpites))
