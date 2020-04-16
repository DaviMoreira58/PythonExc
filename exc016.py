#crie um programa que leia um numero real qualquer pelo teclado e sua posição inteira
#Exp:
#Digite um numero: 6.127
#O numero 6.127 tem a parte inteira 6.
# MEU JEITO
'''from math import trunc
n1 = float(input('digite um numero: '))
n2 = trunc(n1)
print('O numero {} tem a parte inteira {}. '.format(n1, n2))'''

'''import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num))) # caso importe apenas a função trunc'''

#Sem o uso da biblioteca

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
