# Faça um programa que leia um numero inteiro e diga se ele é ou nçao um numero primo
'''
n1 = int(input('Digite um numero qualquer: '))
n2 = 2
n3 = 3
n5 = 5
n11 = 11
p2 = n1 % n2
p3 = n1 % n3
p4 = n1 % n5
p5 = n1 % n11
if(n1 == n2 or n3 == n1 or n5 == n1 or n11 == n1):
    print('{} é primo'.format(n1))
elif(p2 == 0 or p3 == 0 or p4 == 0 or p5 == 0):
    print('{} não é primo'.format(n1))
else:
    print('{} é primo'.format(n1))
'''

num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi dividido {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
