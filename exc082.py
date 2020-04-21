# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.

"""listaT = []
listaP = []
listaI = []
while True:
    n = int(input('Digite um numero: '))
    listaT.append(n)
    r = str(input('Deseja continuar? [S/N] ')).upper()
    if r in 'Nn':
        break
    if n % 2 == 0:
        listaP.append(n)
    if n % 2 == 1:
        listaI.append(n)
print(f'A lista completa é {listaT}')
print(f'A lista de pares é {listaP}')
print(f'A lista de ímpares é {listaI}')"""

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
