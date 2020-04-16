'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

'''n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))
opcao = 0
while opcao != 5:
    if opcao == 1:
        s = n1 + n2
        print('A soma de {} e {} = {}'.format(n1, n2, s))
        opcao = int(input(
\033[33mO que deseja fazer?\033[m
\033[32m[ 1 ] SOMAR\033[m
\033[34m[ 2 ] MULTIPLICAR\033[m
\033[35m[ 3 ] MAIOR\033[m
\033[36m[ 4 ] Novos números\033[m
\033[37m[ 5 ] SAIR DO PROGRAMA\033[m
>>>>  ))
    if opcao == 2:
        m = n1 * n2
        print('A multiplicação de {} por {} = {}'.format(n1, n2, m))
        opcao = int(input(
\033[33mO que deseja fazer?\033[m
\033[32m[ 1 ] SOMAR\033[m
\033[34m[ 2 ] MULTIPLICAR\033[m
\033[35m[ 3 ] MAIOR\033[m
\033[36m[ 4 ] Novos números\033[m
\033[37m[ 5 ] SAIR DO PROGRAMA\033[m
>>>>  ))
    if opcao == 3:
        if n1 > n2:
            print('O {} é maior que o {}'.format(n1, n2))
            opcao = int(input(
\033[33mO que deseja fazer?\033[m
\033[32m[ 1 ] SOMAR\033[m
\033[34m[ 2 ] MULTIPLICAR\033[m
\033[35m[ 3 ] MAIOR\033[m
\033[36m[ 4 ] Novos números\033[m
\033[37m[ 5 ] SAIR DO PROGRAMA\033[m
>>>>  ))
    if n1 < n2:
        print('O {} é maior que o {}'.format(n2, n1))
        opcao = int(input(
\033[33mO que deseja fazer?\033[m
\033[32m[ 1 ] SOMAR\033[m
\033[34m[ 2 ] MULTIPLICAR\033[m
\033[35m[ 3 ] MAIOR\033[m
\033[36m[ 4 ] Novos números\033[m
\033[37m[ 5 ] SAIR DO PROGRAMA\033[m
>>>>  ))
    if opcao == 4:
        n1 = int(input('Digite o 1º numero: '))
        n2 = int(input('Digite o 2º numero: '))
        opcao = int(input(
\033[33mO que deseja fazer?\033[m
\033[32m[ 1 ] SOMAR\033[m
\033[34m[ 2 ] MULTIPLICAR\033[m
\033[35m[ 3 ] MAIOR\033[m
\033[36m[ 4 ] Novos números\033[m
\033[37m[ 5 ] SAIR DO PROGRAMA\033[m
>>>>  ))'''

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print('''    [ 1 ] SOMA
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opçao = int(input('>>>> Qual é a sua opção? '))
    if opçao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opçao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opçao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')


