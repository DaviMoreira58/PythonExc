# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela apareceu a primeira vez
# Em que posição ela aparece a ultima vez

frase = str(input('Qual é a frase? ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))