# Crie um programa que leia o nome inteiro de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro nome

'''nome = str(input('Qual o nome? '))
print(nome.upper())
print(nome.lower())
sem = nome.replace(" ", "")
print(len(sem))
dividido = nome.split()
print(dividido[0])'''

nome = str(input('Digite seu nome completo: ')).strip() # Corta os espaços antes e dps
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
