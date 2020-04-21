# Crie um programa onde o usuario possa digitar vários valores numeeicos e
# cadastre-os em uma lista. Caso o numero já exista dentro, ele nçao será adicionado.
# No final serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    n = int(input('Digite um numero: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não registrado...')
    r = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    if r in 'Nn':
        break
print('-=' * 30)
lista.sort()
print(f'Você digitou os valores {lista}')
