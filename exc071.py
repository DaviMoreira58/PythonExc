# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio,
# pergunte ao usuario qual será o valor a ser sacado (números inteiros) e o programa vai
# informar quantas células de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
# To zuado em lista

print('=' * 30)
print('{:^30}'.format('BANCO DAVI'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao banco DAVI! Tenha um bom dia!')
