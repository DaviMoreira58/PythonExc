# Desenvolva um programa que leia quatro valores pelo teclado e guadeos em uma tupla. Nofonal, mostre:
# A) Quantas vezes o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os numeros pares.

"""n0 = int(input('Digite um valor: '))
n1 = int(input('Digite outro valor: '))
n2 = int(input('Digite mais um valor: '))
n3 = int(input('Digite o ultimo valor: '))
tupla = (n0, n1, n2, n3)
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)}ª posição')
else:
    print('O valor 3 não apareceu')
while tupla % 2 == 0:
    print(tupla)""" # Meu jeito

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
       print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
       print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for n in num:
       if n % 2 == 0:
              print(n, end=' ')
