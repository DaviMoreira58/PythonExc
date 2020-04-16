#Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.
#   MEU JEITO
#n1 = int(input('Digite um numero: '))
#n2 = n1 * 1
#n3 = n1 * 2
#n4 = n1 * 3
#n5 = n1 * 4
#n6 = n1 * 5
#n7 = n1 * 6
#n8 = n1 * 7
#n9 = n1 * 8
#n10 = n1 * 9
#n11 = n1 * 10
#print('Tabuada do {}: \n x1: {} \n x2: {} \n x3: {} \n x4: {} \n x5: {} \n x6: {} \n x7: {} \n x8: {} \n x9: {} \n x10: {}'.format(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11))

# JEITO DA RESOLUÇÃO
num = int(input('Digite um numero para ver a sua tabuada: '))
print('\033[1;33m_\033[m' * 14)
print('{} x {:2} = {}'. format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('\033[1;33m_\033[m' * 15)