# Crie um programa que mostre na rela todos os numeros pares que estão no intervalo
# entre 1 e 50.

'''for c in range(0, 51, 2):
    print(c)'''

'''for n in range(0, 51):
    print('.', end='') # verifica quantos laços estçao sendo executados, nesse caso ele executa duas vezes para aparecer uam variavel
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou')'''

for n in range(2, 51, 2):
    print('.', end='') # Aqui indica que ele fez metade das repetiçoes, ocupando o processador metade do tempo
    print(n, end=' ')
print('Acabou!')