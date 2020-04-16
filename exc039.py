# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda vai se alistar no serviço militar
# Se é a hora de se alistar
# Se já passou do tempo de alistamento
# Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
print('\033[35mALISTAMENTO\033[m')
'''idade = int(input('Qual é a sua idade? '))
if idade > 18:
    n1 = idade - 18
    print('Voce ja passou {} anos do alistamento'.format(n1))
elif idade < 18:
    n2 = 18 - idade
    print("faltam {} anos para se alistar".format(n2))
elif idade == 18:
    print('Você precisa se alistar')'''

'''atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))'''

atual = date.today().year
sexo = int(input('''Por gentileza, selecione o numero que correspode ao seu sexo
[ 1 ] Feminino
[ 2 ] Masculino'''))
if sexo == 1:
    print('Você não precisa se alistar obrigatoriamente!')
if sexo == 2:
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
