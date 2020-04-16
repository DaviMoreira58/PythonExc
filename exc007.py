#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = (n1 + n2) / 2
print ('A sua média é de \033[4;34m{}\033[m'.format(n3))