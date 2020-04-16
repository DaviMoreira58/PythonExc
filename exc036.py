# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salario do comprador e quantos anos ele
# vai pagar. Calcule o valor da prestaçaõ mensal, sabendo que ela não pode exeder
# 30% do salário ou então o empréstimo será negado.

'''casa = float(input('Qual é o valor da casa escolhida? '))
salario = float(input('Qual é o valor do salario? '))
anos = int(input('Em quantos anos pretende pagar? '))
meses = anos * 12
parcelas = casa / meses
if parcelas > (salario * 30 /100):
    print('Não podemos aprovar o seu empréstimo!')
else:
    print('Parabens, seu empréstimo foi aprovado!!')'''

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 /100
print('Para pagar uma casa de R${:.2f} em {} anos,'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO')
