# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o
# maior e menor peso lidos.

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi e {}Kg'.format(menor))

'''lst=[]  #lista vazia
for c in range(1, 6):
    peso=float(input('Peso da {}ª pessoa: '.format(c)))
    lst+=[peso]   #adc os valores de peso na lista
print('')
print('O Maior peso foi:', max(lst))  #maximo valor da lista
print('O Menor peso foi:', min(lst))  #minimo valor da lista'''