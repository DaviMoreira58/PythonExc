# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão
# De zero até vinte.
# Seu programa deverá ler o numero pelo teclado(entre 0-20) e mostra-lo por extenso

pos = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
       'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete',
       'Dezoito', 'Dezenove', 'Vinte')
for num in range(0, 20):
    num = int(input('Digite um numero entre 0 e 20: '))
    if num >= 0 and num <= 20:
        print(f'Você digitou o numero {pos[num]}')
        break
    '''else:
        num = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
        if num >= 0 and num <= 20:
            print(f'Você digitou o numero {pos[num]}')
            break'''