# Faça um programa que calcule a soma entre todos os numero impares que são multiplos
# de tres e que se encontram no intervalo de 1 até 500.

'''for c in range(1, 500):
    n = c % 3
    if n == 0:
        print(c)''' # Erro

'''for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')''' # Mostra os multiplos de 3

'''soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
print('A soma de todos os calores solicitados é {}'.format(soma))'''

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # ou 'cont += 1'
        soma = soma + c # ou 'soma += c'
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
