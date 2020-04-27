# Faça um programa que leia nome e peso de várias pessoas, guardnado tudo em uma lista. No final mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
dados = list()
tot = 0
pesados = 0
leves = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    tot += 1
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if pessoas[1] >= 100:
        pesados += 1
    if continuar in 'Nn':
        break

print(pessoas)
print(f'Foram cadastradas {tot} pessoas.')
print(f'{pesados} pessoas estão acima do peso.')
print(f'{leves} pessoas estão abaixo do peso.')