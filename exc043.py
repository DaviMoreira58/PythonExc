# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e
# mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 15.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

'''peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura * altura)
if imc <= 18.5:
    print('Seu IMC é de {:.2f} e você está abaixo do peso'.format(imc))
elif imc <= 25:
    print('Seu IMC é de {:.2f} e você está no peso ideal'.format(imc))
elif imc <= 30:
    print('Seu IMC é de {:.2f} e você está com sobrepeso'.format(imc))
elif imc <= 40:
    print('Seu IMC é de {:.2f} e você está com obesidade'.format(imc))
elif imc > 40:
    print('Seu IMC é de {:.2f} e você está com obesidade mórbida'.format(imc))'''

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc =peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc <= 25:
    print('Parabens, você está na faixa de PESO NORMAL')
elif 25 <= imc <= 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!!')
