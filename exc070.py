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

total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor: # esse 'or preço < menor:' eliminou o else inteiro! Genial
        menor = preço
        barato = produto
#    else:
#        if preço < menor:
#            menor = preço
#            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')
