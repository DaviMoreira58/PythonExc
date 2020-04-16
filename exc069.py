# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuario quer ou não continuar. No final mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos

"""cont = maiores = meninas = homens = idade = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    opçao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while opçao not in 'SsNn':
        opçao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    print('-' * 20)
    if idade > 18:
        maiores += 1
    if idade < 20 and sexo in 'Ff':
        meninas += 1
    if sexo in 'Mm':
        homens += 1
    if opçao in 'Ss':
       cont += 1
    else:
        break
print('=' * 20)
print(f'{maiores} pessoas são maiores de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{meninas} são mulheres com menos de 20 anos.')
print('=' * 20)""" # Meu jeito

tot18 = totH = totM20 =  0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
