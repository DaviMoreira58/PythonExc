# Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final, mostre qual foi o menor e qual foi o maior valr digitado e as suas
# respectivas posiçãoes na lista


valores = list()
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
        print(f'{c}... ', end='')