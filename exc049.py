# Refaça o DESAFIO 009, mostrando a tabuada de um numeor que o usuario escolher,
# so que agora utiliznaod um laço for

'''num = int(input('Digite um numero: '))
for x in range(1, 11):
    total = num * x
    print('{} x {:2} = {}'.format(num, x, (total)))'''

num = int(input('Digite um número para ver a sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
