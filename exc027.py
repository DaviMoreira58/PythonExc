# Faça um programa que leia o nome completo de uma pessoa, mostre em seguida o
# primeiro e ultimo nome separadamente
# Exp: Ana Maria de Souza
# Primeiro = Ana
# Ultimo = Souza

'''nome = str(input('Qual é o seu nome? '))
dividido = nome.split()
print('Primeiro nome: {}'.format(dividido[0]))
print('Ultimo nome é: {}'.format(dividido[3]))'''


n = str(input('Qual é o seu nome completo? ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))


