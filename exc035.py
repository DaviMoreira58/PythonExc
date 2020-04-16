# Desenvolva um programa que leia o comprimento de três retas e difa ao usuario se elas podem ou
# não formar um triangulo

'''a = int(input('Reta n 1: '))
b = int(input('Reta n 2: '))
c = int(input('Reta n 3: '))

a1 = (b - c) < a < b + c
b1 = (a - c) < b < a + c
c1 = (a - b) < c < a + b
if a1 == True and b1 == True and c1 == True:
 print('Poode ser feito um triangulo')
else:
 print('Nao pode ser feito um triagulo')'''

print('\033[32m-=-'*20)
print('\033[35mAnalisador de triangulos')
print('\033[32m-=-\033[m' *20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
 print('\033[32;1mOs seguimentos acima PODEM FORMAR triangulo!\033[m')
else:
 print('\033[35;1mOs segmentos acima NÃO PODEM triangulo\033[m')