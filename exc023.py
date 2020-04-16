# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
# Exp: Digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

'''numero = str(input('Digite um número de quatro digitos: '))
unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(unidade, dezena, centena, milhar))'''

'''num = int(input('Informe um numero: '))
n = str(num)
print('Analisando o numero: {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))'''

num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero: {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))