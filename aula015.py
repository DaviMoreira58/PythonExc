'''
                        LAÇOS DE REPETIÇÕES
                            (Parte 3)

O exemplo foi agora que exite um troféu no nivel superior, se ele achar esse trofeu
ele irá pega-lo e ganhar o jogo.

enquanto Verdadeiro:            while True:
    se[terra]:                      if[terra]:
        passo                           passo
    se[vazio]                       if[vazio]
        pula                            pula
    se[moeda]                       if[moeda]
        pega                            pega
    se[trofeu]                      if[trofeu]
        pula                            pula
        interrompa                      break
pega                            pega

    Exemplos praticos

cont = 1
while True:
    print(cont, '→', end='')
    cont += 1
print('Acabou')


n = 0
while n != 999:
    n = int(input('Digite um numero: '))

n = cont = 0
while cont < 3:
    n = int(input('Digite um numero: '))
    cont += 1

n = s = 0
while n != 999:
    n = int(input('Digite um numero: '))
    s += n
s -= 999                                    # Gambiarra
print('A soma vale {}'.format(s))

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break                               # Sem gambiarra
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')                  # F strings, substitui o '.format'

nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.')            # Novo jeito PYTHON 3.6+
print('O {} tem {} anos.'.format(nome, idade))  # Jeito que aprendi # PYTHON 3
print('O %s tem %d anos' % (nome, idade))       # Jeito antigo PYTHON 2

nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')
print(f'O {nome:20} tem {idade} anos e ganha R${salario:.2f}') # Com 20 espaços
print(f'O {nome:^20} tem {idade} anos e ganha R${salario:.2f}') # Com 20 espaços e centralizado
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}') # preenchido com '-'
print(f'O {nome:->20} tem {idade} anos e ganha R${salario:.2f}') # alinhado a direita
print(f'O {nome:-<20} tem {idade} anos e ganha R${salario:.2f}') # alinhado a esquerda
























'''