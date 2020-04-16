# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

'''ano = int(input('Qual é o ano? '))
if ano % 4 > 0:
    print('O ano de {} não é bissexto.'.format(ano))
else:
        print('O ano de {} é bissexto.'.format(ano))'''
from datetime import date
ano = int(input('Que ano quer analisar? Coloque \033[32m0\033[m para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano \033[35;4m{}\033[m é BISSEXTO'.format(ano))
else:
    print('O ano \033[36;4m{}\033[m NÃO É BISSEXTO'.format(ano))