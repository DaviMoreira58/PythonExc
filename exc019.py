# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido
'''import random
n1 = input('Qual o é primeiro nome? ')
n2 = input('Qual o é segundo nome? ')
n3 = input('Qual o é terceiro nome? ')
n4 = input('Qual o é quarto nome? ')
1 == n1                                 #o nome não aparece
2 == n2
3 == n3
4 == n4
ale = random.randint(1, 4)
print('O aluno sorteado foi {}'.format(ale))'''

'''import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))'''

'''from random import choice
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome '))
n4 = str(input("Quarto nome: "))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O escolhido foi {}'.format(escolhido))'''