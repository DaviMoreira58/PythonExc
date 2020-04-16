#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor

n1 = int(input('Digite um numero: '))
n2 = n1 - 1
n3 = n1 + 1
print('O antecessor de \033[1;32m{}\033[m é \033[1;34m{}\033[m e o sucessor é \033[33;1m{}\033[m'.format(n1, n2, n3))