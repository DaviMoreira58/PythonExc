# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar. No final mostre:
# Qual é o gasto total na compra.
# Quantos produtos custram mais de R$ 1000,00
# Qual é o nome do produto mais barato.

"""cont = soma = menor = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = int(input('Preço: '))
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    soma += preço
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if preço >= 0:
        maior = menor = preço
    else:
        if preço < menor:
            menor = preço
    if preço > 1000:
        cont += 1
    if continuar in 'Nn':
        break
print(cont)
print(soma)
print(f'{menor}')""" # Não terminei


