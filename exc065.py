# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
cont = media = soma = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    cont += 1
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont == 1:
       maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print('Voce digitou {} e a media é {:.2f}'.format(cont, media))
print('O maior numero foi {} e o menor foi {}'.format(maior, menor))


