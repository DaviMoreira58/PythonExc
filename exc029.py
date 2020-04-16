# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
# mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 para cada Km acima do limite.

velocidade = int(input('Qual é a velocidade? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('\033[31mVoce foi multado em R${},00'.format(multa))
else:
    print('\033[1;30mVoce não foi multado\033[m')