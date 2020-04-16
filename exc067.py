# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
# valor digitado pelo usuario. O programa será imterrompido quando o numero solicitado
# for negativo.

"""while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n >= 0:
        print('=' * 20)
        cont = 0
        while cont < 10:
            cont += 1
            mult = n * cont
            print(f'{cont} x {n} = {mult}')
        print('=' * 20)
    if n < 0:
        break
print('\033[34;4mPROGRAMA TABUADA ENCERRADO. Volte sempre!')""" # Meu jeito

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
