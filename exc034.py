# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
# para salarios superiores a 1250 calcule 10%, inferiores ou igual 15%

'''sal = float(input('Qual é o salario? '))
if sal >= 1250.00:
    aum1 = sal * 0.1
    sal1 = aum1 + sal
    print('o salario subiu para {:.2f}'.format(sal1))
else:
    aum2 = sal * 0.15
    sal2 = aum2 + sal
    print('o salario subiu para {}'.format(sal2))'''

salario = float(input('Qual é o salario do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava \033[31mR${:.2f}\033[m passa a ganhar \033[34mR${:.2f}\033[m agora'.format(salario, novo))