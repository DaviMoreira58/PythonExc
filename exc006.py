#Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

n1 = int(input("Digite um numero: "))
n2 = n1 * 2 # d
n3 = n1 * 3 # t
n4 = n1 ** (1/2) # r
print('O dobro de \033[7;30m{}\033[m é \033[31;1m{}\033[m. '.format(n1, n2,))
print('O triplo de \033[7;30m{}\033[m é \033[32;1m{}\033[m. '.format(n1, n3))
print('A raiz quadrada de \033[7;30m{}\033[m é \033[33;1m{:.2f}\033[m. '.format(n1, n4))