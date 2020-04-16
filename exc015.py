# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado

n1 = int(input('Quantos dias foi alugado? '))
n2 = float(input('Quanto Km foram percorridos? '))
dia = n1 * 60
km = n2 * 0.15
valor = dia + km
print('O valor total do aluguel é de {} reais'.format(valor))