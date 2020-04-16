# Desenvolva um peograma que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem
# cobrada RS0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas.

'''km = int(input('Qual a distancia? '))
if km < 200:
    calc1 = km * 0.5
    print('Voce ira pagar R${:.2f}'.format(calc1))
else:
    calc2 = km * 0.45
    print('Voce irá pagar R${:.2f}'.format(calc2))'''

'''distancia = float(input('Qual é a distancia da sua viagem? '))
print('Voce esta prestes a começar um viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''

distancia = float(input('Qual é a distancia? '))
print('Voce está prestes a começar um viagem de {}Km'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))