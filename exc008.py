#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

n1 = float(input('\033[1;36mQuantos metros?\033[m '))
n2 = n1 * 100
n3 = n1 * 1000
print('{} \033[1;35mem centimetros é\033[m {} \033[1;33me em milimetros é\033[m {}'.format(n1, n2, n3))