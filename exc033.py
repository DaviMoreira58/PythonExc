# Faça um porgrama que leia tres numeros e mostre qual é o maior e qual é o menor
'''
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))'''

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > a:
    maior = c
print('O menor valor digitado foi \033[32;4m{}\033[m'.format(menor))
print('O maior valor digitado foi \033[36;4m{}\033[m'.format(maior))
