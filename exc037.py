# Escreva um programa que leia um número inteiro qualquer e peça para que leia um nuúmero
# inteiro qualquer e o usuario escolha qual será a base de conversão:
# 1 para binario
# 2 para octal
# 3 para hexadecimal

'''from pythonds.basic.stack import Stack
n1 = int(input('Qual valor deseja converter? '))
n2 = int(input('Ok, para qual base? 1 = Binário; 2 = Octal; 3 = Hexadecimal '))
if n2 == 1:                     não consegui
    binario = Stack(n1)
    print(binario)'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das baser para conversão:
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente.')