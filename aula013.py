'''
                    ESTRUTURAS DE REPETIÇÕES OU LAÇOS DE REPETIÇÃO
# Estrutura de repetição com varialvel de controle (FOR)

  o exemplo usado é um personagem andando da casa 0 a 10. Onde a maça se encontra no 10

Laço com variavel de controle:
        em portugues                        no python
    laço c no intervalo(1,10)          for c in range(1, 10):
        passo                              passo
    pega                                pega

o exemplo é um personagem percorrendo as casas mais a cada duas exixte um buraco
ele precisa fazer a oepração de andar e pular tres vezes seguidas:

laço c no intervalo(0,3)            for in c range(0, 3):
    passo                               passo
    pula                                pula
passo                               passo
pega                                pega

substitui esse:
passo
pula
passo
pula
passo
pula
passo
pega

exemplo é o mesmo de cima mais no primeiro e ultimo pulo precisa pegar uma moeda = ♦

laço c no intervalo(0,3)            for c in range(0, 3):
    se ♦                                if ♦:
        pega                                pega
    passo                               passo
    pula                                pula
passo                               passo
pega                                pega

escrever 'oi' seis vezes:
for c in range(1, 6): #desse jeito ele faz cinco, pois não considera que tem que ir até 6, mas sim 5
for c in range(0, 6): # desse jeito faz 6 vezes
    print('oi')
print('FIM')

========
for c in range (0, 6):              for c in range (1, 7):
    print(c) # escreve de 0 a 5         print(c) # escreve de 1 a 6
print('FIM')                        print('FIM')
=======
Quer contar de 6 a 0:

for c in range(6, 0):                   for c in range(6, 0, -1):
    print(c) # só escreve FIM               print(c) # o -1 significa qual é a iteração, 6, 5 ,4...
print('FIM')                            print('FIM')
=======
for c in range(0, 7, 2):
    print (c) # 0;2;4;6
print('FIM')
===========

n = int(input('Digite um número:'))
for c in range(0, n+1): # para chegar no valor de input
    print(c)
print('FIM')

==============

i = int(input('Início: '))  # numero inicial
f = int(input('Fim: '))     # numero final
p = int(input('Passo: '))   # intervalo de "Pulo"
for c in range(0, f+1, p):
    print(c)
print('FIM')

==============

for c in range(0, 3):
    n = int(input('Digite um valor: ')) # vai repetir tres vezes a pergunta. Mto util
print('fim')

=============

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n # substitui s = s + n
print('O somatorio de todos os valores foi {}'.format(s))

==============














































'''