#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de descontp

n1 = int(input('Qual o valor do produto? '))
n2 = n1 * 0.05
# n2 = n1*5/100
n3 = n1 - n2
print('O valor com o desconto é de {}'.format(n3))