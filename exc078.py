# Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final, mostre qual foi o menor e qual foi o maior valr digitado e as suas
# respectivas posiçãoes na lista


"""valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor para a posição {cont}: ')))
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f'{c}... ', end='')
print(f'\nO menor valor digitado foi {min(valores)} na posição ', end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f'{c}... ', end='')""" # Meu jeito

listanum = []
mai = men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c} ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('-=' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado doi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
