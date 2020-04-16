# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida.
# Média abaixo de 5.0: Repreovado
# Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado

'''n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
med = (n1 + n2) / 2
if med <= 5.0:
    print('Sua média foi {} \033[031;1mREPROVADO\033[m'.format(med))
elif med <= 6.9:
    print('Sua média foi {} \033[32;1mRECUPERAÇÃO\033[m'.format(med))
elif med >= 7.0:
    print('Sua média foi {} \033[35;1mAPROVADO\033[m'.format(med))
else:
    print('Digite algo')'''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:
# if media >= 5 and media <7:
    print('O aluno está  em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO.')
else: # elif media >= 7:
    print('O aluno está APROVADO')

