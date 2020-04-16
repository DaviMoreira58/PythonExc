# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido
# quando o jogador PERDER, mostrando o total de vitorias consecutivas que ele
# conquistou no final do jogo.

"""from random import randint
soma = cont = 0
while True:
    jogador = int(input('Digite um valor: '))
    pc = randint(0, 10)
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = jogador + pc
    print('=' * 20)
    cont += 1
    if soma % 2 == 0 and escolha in 'Pp':
        print(f'Voce jogou {jogador} e o computador {pc}. Total de {soma} DEU PAR')
        print('Você venceu!')
        print('Vamos jogar novamente...')
        print('=' * 20)
    elif soma % 2 != 0 and escolha in 'Ii':
        print(f'Voce jogou {jogador} e o computador {pc}. Total de {soma} DEU IMPAR')
        print('Você venceu!')
        print('Vamos jogar novamente...')
        print('=' * 20)
    else:
        break
        print('=' * 20)
print(f'GAME OVER! Você ganhou {cont} vezes.')
print(f'Voce jogou {jogador} e o computador {pc}. Total de {soma}')""" # Meu jeito

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ',end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
