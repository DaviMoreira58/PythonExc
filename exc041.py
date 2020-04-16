# A fonfederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria de acordo com a idade
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SENIOR
# Acima: MASTER

'''from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
if idade <= 9:
    print('Você é da categoria MIRIM')
elif idade <= 14:
    print('Você é da categoria INFANTIL')
elif idade <= 19:
    print('Você é da categoria JUNIOR')
elif idade <= 25:
    print('Você é da categoaria SÊNIOR')
elif idade > 25:
    print('Você é da categoaria MASTER')'''

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
