# Crie um programa que leia o nome de uma cidade e diga se ela começa ou ñ com o nome
# "SANTO"

'''cidade = str(input('Qual o nome da cidade? '))
resultado = cidade.find("Santo")
if resultado < 0:
    print('Não tem')
elif resultado < 2:
    print('começa')
elif resultado < 100:
    print('Não começa')'''

cid = str(input('Em que cidade voce nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')