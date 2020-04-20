# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
# preços na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

"""lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Tranferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)

x = 0
y = 1
for cont in range(0, len(lista)):
    print(f'{lista[x]:.<20}R${lista[y]:8}')
    x += 2
    y += 2""" # Meu jeito

listagem = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Tranferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livros', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
