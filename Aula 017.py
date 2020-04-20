"""
                        VARIAVEIS COMPOSTAS
                               LISTAS
                              (Parte 1)

Tuplas ()
Listas []

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
lache[3] = 'Picole'
→ Erro, pois TUPLAS são imutaveis

lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche[3] = 'Picole'
→ Dá certo, porque LISTAS são mutaveis!
* Sem a função 'append' não é possivel adicionar espaços na LISTA

→ lanche.append('cookie')
adiciona o cookie a LISTA no final da lista. Antes existiam apenas 4 espasos, agora 5.

→ lanche.insert(0,'Cachorro quente')
                ↑→ adicionou o cachorro quente na posição 0. Anteriormente
                do hamburguer, assim, fazendo todos se deslocarem.
        lanche
        │CACHORRO QUENTE│HAMBURGUER│SUCO│PIZZA│SORVETE│COOKIE│
                0           1         2    3     4       5

Para eliminar:
    del lanche[3]
    lanche.pop(3) → Normalmente utilizado para eliminar o ultimo elemnto, mas pode
               ↑    ser usado com o parametro o indice que desejo eliminar
    lanche.remove('Pizza') → Nesse comando não indicamos o indice, é indicado o
                     ↑       valor que desejo eliminar

                    EM TODOS ESSES CASOS ACONTECE:
        lanche
        │CACHORRO QUENTE│HAMBURGUER│SUCO│SORVETE│COOKIE│
                0           1         2     3      4

*Se ursar o lanche.pop() isolado:
                       ↑
        lanche
        │CACHORRO QUENTE│HAMBURGUER│SUCO│SORVETE│                   ←
                0           1         2     3                       ↑
                                                                    ↑
→ E se eu tentar remover um item inexistente?                       ↑
  Exp.:> lanche.remove('Pizza') # Lembrando que ele já foi excluido ↑

                Acontece um erro da linguagem!

Para resolver isso:
if 'Pizza' in lanche:
    lanche.remove('Pizza')

→→→ É POSSIVEL CRIAR LISTAS APARTIR DE RANGES

valores = list(range(4, 11))

        valores
        │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 10 │
          0   1   2   3   4   5    6

valore = list(range(4, 11, 2))
        valores
        │ 4 │ 7 │ 10 │
          0   1   2

valores = [8, 2, 5, 4, 9, 3, 0]
        valores
        │ 8 │ 2 │ 5 │ 4 │ 9 │ 3 │ 0 │
          0   1   2   3   4   5   6

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
        valores
        │ 0 │ 2 │ 3 │ 4 │ 5 │ 8 │ 9 │
          0   1   2   3   4   5   6

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
valores.sort(reserve = True)
        valores
        │ 9 │ 8 │ 5 │ 4 │ 3 │ 2 │ 0 │
          0   1   2   3   4   5   6

valores = [8, 2, 5, 4, 9, 3, 0]
len(valores) # == 7
        valores
        │ 9 │ 8 │ 5 │ 4 │ 3 │ 2 │ 0 │
          0   1   2   3   4   5   6

PRATICA

num = (2, 5, 9, 1)
num[2] = 3
print(num)
→Erro

num = [2, 5, 9, 1]
num[2] = 3
print(num)
→[2, 5, 3, 1]

num = [2, 5, 9, 1]
num[2] = 3
num[4] = 7
print(num)
→Erro

num = [2, 5, 9, 1]
num[2] = 3
num.append = 7
print(num)
→[2, 5, 3, 1, 7]

num = [2, 5, 9, 1]
num[2] = 3
num.append = 7
num.sort()
print(num)
→[1, 2, 3, 5, 7]

num = [2, 5, 9, 1]
num[2] = 3
num.append = 7
num.sort(reverse=True)
print(num)
→[7, 5, 3, 2, 1]

num = [2, 5, 9, 1]
num[2] = 3
num.append = 7
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
→[7, 5, 3, 2, 1]
→ Essa lista tem 5 elementos.

num = [2, 5, 9, 1]
num[2] = 3
num.append = 7
num.sort(reverse=True)
num.insert(2, 0)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
→[7, 5, 0, 3, 2, 1]
→ Essa lista tem 6 elementos.

num = [2, 5, 9, 1]
num[2] = 3
num.append = 7
num.sort(reverse=True)
num.insert(2, 0)
num.pop()
print(num)
print(f'Essa lista tem {len(num)} elementos.')
→[7, 5, 0, 3, 2]
→ Essa lista tem 5 elementos.

num = [2, 5, 9, 1]
num[2] = 3
num.append = 7
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
→[7, 5, 3, 2, 1]
→ Essa lista tem 5 elementos.

num = [2, 5, 9, 1]
num[2] = 3
num.append = 7
num.sort(reverse=True)
num.insert(2, 2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
→[7, 5, 2, 3, 2, 1]
→ Essa lista tem 6 elementos.

num = [2, 5, 9, 1]
num[2] = 3
num.append = 7
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2) → # Remove o primeiro 2. Ele procura do primeiro item da lista até achar o que deseja ser eliminado, independente se houver mais
print(num)
print(f'Essa lista tem {len(num)} elementos.')
→[7, 5, 3, 2, 1]
→ Essa lista tem 5 elementos.

num = [2, 5, 9, 1]
num[2] = 3
num.append = 7
num.sort(reverse=True)
num.insert(2, 2)
num.remove(4)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
→ Erro

num = [2, 5, 9, 1]
num[2] = 3
num.append = 7
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
→ Não achei o numero 4
→[7, 5, 2, 3, 2, 1]
→ Essa lista tem 6 elementos.

num = [2, 5, 9, 1]
num[2] = 3
num.append = 7
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o numero 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
→[7, 2, 3, 2, 1]
→ Essa lista tem 5 elementos.

_____________________________________________________________________
* É possivel começar listas vazias de duas formas no python:

valores = []
  ou
valores = list()
______________________________________________________________________

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
→print('Cheguei ao final da lista')
→Na posição 0 encontrei o valor 5!
→Na posição 1 encontrei o valor 9!
→Na posição 2 encontrei o valor 4!
→Cheguei ao final da lista

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a
print(a)
print(b)

a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}')
print(f'Lisya B: {b}')
→Lista A: [2, 3, 4, 7]
→Lisya B: [2, 3, 4, 7]

a = [2, 3, 4, 7]
b = a →→ Dessse jeito é uma ligação
b[2] = 8 # Não altera só a B pois o python faz uma ligação entre listas
print(f'Lista A: {a}')
print(f'Lisya B: {b}')
→Lista A: [2, 3, 8, 7]
→Lista B: [2, 3, 8, 7]

a = [2, 3, 4, 7]
b = a[:]→ Assim copiamos todos os item de 'a' na lista 'b', assim nçao existe uma ligação e sim uma cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
→Lista A: [2, 3, 4, 7]
→Lista B: [2, 3, 8, 7]

"""