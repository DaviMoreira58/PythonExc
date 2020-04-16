# Crie um programa que leia varios numeros inteiros pelo teclaod. O programa só vai parar
# quando o usuario digitar o valor 999, que é a condição de parada. No final mostre
# quantos numeros foram digitados e qual foi a soma entr eles (desconsiderando o flag)

"""s = c = 0
while True:
    n = int(input('Difite um valor (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores é {s}!')""" # Meu jeito

"""num = soma = 0
while num != 999:
    num = int(input('Digite um valor (999 para parar): '))
    soma += num
soma -= 999
print(f'Acabou soma dos valores foi {soma}!')""" # Gambiarra

soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}')