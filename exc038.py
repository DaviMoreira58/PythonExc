# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela a mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

print('\033[34mCOMPARADOR DE NUMEROS\033[m')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('O primeiro valor é o maior')
elif n2 > n1:
    print('O segundo valor é maior')
elif n2 == n1:
    print('Não existe valor maior, os dois são iguais')
