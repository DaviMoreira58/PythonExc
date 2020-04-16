# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N
# primeiros elementos de uma Sequência de Fibonacci.

'''print('-' * 25)
print('Sequencia de Fibonacci')
print('-' * 25)
n = int(input('Quantos termos você quer mostrar? '))
c = 0
f = 0
while c <= n:
    print('{}'.format(f))
    m = f + 1
    c += 1'''
print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print('~' * 30)
print('{} → {}'.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
print('~' * 30)
