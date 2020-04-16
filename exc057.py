# faça um porgrama que leia o sexo de uma pessoa, mas só acite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

'''sexo = str(input('Informe seu sexo: [M/F] ')).upper()
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).upper()
print('Sexo {} registrado com sucesso'.format(sexo))'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Pr favor, Informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))