# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

'''nome = str(input('Qual o seu nome? '))
resultado = nome.find("Silva")
if resultado < 0:
    print('não tem')
elif resultado < 100:
    print('Tem silva no nome')'''

nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper())) # ou 'silva' in nome.lower()
