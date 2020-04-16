# Desenvolva um programa que leia seis numeros inteiros e mostre na tela apenas os que
# forem pares. Se o valor digitado for impar. desconside-o

'''for c in range(0, 6):
    n = int(input('Digite um valor: '))
    p = n % 2
print(c)''' # Errado

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0: # é esse if que separa os pares
        soma += num
        cont += 1
print('Você informaou {} números PARES e a soma foi {}'.format(cont, soma))