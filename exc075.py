# Desenvolva um programa que leia quatro valores pelo teclado e guadeos em uma tupla. Nofonal, mostre:
# A) Quantas vezes o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os numeros pares.

n0 = int(input('Digite um valor: '))
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
    print(tupla)


