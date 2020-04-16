# Elabore um programa que calcule o valor a ser pago por um porduto, considerando o
# seu oreço normal e condição de pagamento:
# A vista: dinheiro / cheque: 10% de desconto
# A vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

'''cores = {'limpa':'\033[m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33',
         'azul':'\033[1;34m'}
produto = float(input('Qual o valor do produto? R$ '))
pagamento = int(input(Qual a forma de pagamento?
 [ 1 ] DINHEIRO
 [ 2 ] CHEQUE
 [ 3 ] CARTÃO
 > ))
if pagamento == 1 or 2:
    custo = produto - (produto * 10 / 100)
    print('O produto teve um desconto de 10% e ficou em R${}'.format(custo))
if pagamento == 3:
    x1 = int(input(A vista ou parcelado?
    [ 1 ] A vista 5% de desconto
    [ 2 ] 2x s/ juros
    [ 3 ] 3x com 20% de juros
    > ))
    if x1 == 1:
        custo = produto - (produto * 5 /100)
        print('O protudo teve um desconto de 5% e ficou em R%{}'.format(custo))
    if x1 == 2:
        custo = produto / 2
        print('Cada percela custará R${}'.format(custo))
    if x1 == 3:
        custo = (produto + (produto * 20 /100)) / 3
        print('Cada parcela custará R${}'.format(custo) )'''

print('{:=^40}'.format(' LOJAS MOREIRA '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preço - (preço * 10 / 100)
elif opcao == 2:
    total = preço - (preço * 5 /100)
elif opcao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO INVALIDA de pagamento. Tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
