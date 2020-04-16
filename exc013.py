#faça um algoritimo que leia o salário de um funcionario e mostre seu novo salario com 15% de aumento

n1 = float(input('Qual é o seu salario? '))
n2 = n1 * 0.15
#  n1 + (n1 * 15/100)
n3 = n1 + n2
print('Agora seu salario é de {:.2f}'.format(n3))