#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#Considere US$1.00=R$3,27

n1 = float(input('Quantos reais você quer converter? '))
n2 = n1 / 3.27
print('Você pode comprar \033[32;1mUS${:.2f}'.format(n2))