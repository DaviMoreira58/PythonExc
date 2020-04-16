# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
# de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
'''for c in range(11, 0, -1):
    print(c  - 1)
    sleep(1)
print('BOOOOM')'''
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('BUM! BUM! POOOW!')