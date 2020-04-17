"""
                             VARIAVEIS COMPOSTAS
                                 (TUPLAS)

Em Python existem 3 tipos de variaveis compostas, TUPLAS, LISTAS e os DICIONARIOS.

O que é uma variavel composta?
Em uma variavel normal, exixte o "espaço" apenas para uma atribuição. Exemplo:

    lanche = Hamburguer
                            O espaço da variavel 'lanche' foi preenchido por 'hamburguer'

Quero tomar 'suco' com o meu 'hamburguer'

    lanche = Suco
                            O espaço da variavel 'lanche' foi substituido por 'Suco'

Ou seja, não será possivel ter o 'hamburguer' e o 'suco' com uma variavel simples.


O que é uma Tupla?

É uma variavel que guarda n valores.
Exp.:
                        Lanche(tem 4 variaves)
        'hamburguer' 'suco' 'pizza' 'pudim'
             0          1      2       3

print(lanche[2])
== 'pizza'

print(lache[0:2])
== 'hamburguer' e 'suco'

print(lanche[1:]) vai do 1 até o final
== 'suco' 'pizza' 'pudim'

print(lanche[-1]) é o ultimo elemento
== 'pudim'

print(lanche[-2]) seria o penultimo
== 'pizza'

print(lanche[-3])
== 'suco'

podemos usar 'len' em uma TUPLA ou coleçoes, len se refere a comprimento.

len(lanche) é como se fosse → Quantos quadrados(espaços) tem no lanche?
== 4

for c in lanche: → Para cada comida(C) no lanche:    * Ñ existia a variavel "c", então o python cria e ela é simples
    print(c) → Para cada comida ele ira declarar
==  'Hamburguer'
    'Suco'
    'Pizza'
    'Pudim'
→ e acaba

Quero trocar o pudim por sorvete. Não é possivel alterar uma tupla

                       "AS TUPLAS SÃO IMUTÁVEIS!!!!"

Quando o programa está rodando! Para altera-lá é necessario parar o programa e
fazer a alteração!

                Parte pratica da Aula:

podemos inicar uma varialvel composta de 3 maneiras
lanche = () == Tupla
lanche = [] == Lista
lanche = {} == Dicionario

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim' # No Python novo não precisa de parenteses
print(lanche)

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1]) # Na hora de referenciar sempre é utilizado →[]

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-2])

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1:3]) # Do elemento 1 ao 3 sendo o pudim ignorado

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[2:]) # Do elemento 2 até o final

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[:2]) # Me do primeiro elemento até o 2, ignorando a pizza

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-2:]) # Começa no 2 e vai até o final

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')   ╗
lanche[1] = 'Refrigerante'                          ╠== Isso gera um erro, afirmando que uma tupla não pode ter itens atribuidos
print(lanche[-2:])                                  ╝

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(comida)
┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')   ╗
for comida in lanche:                               ╠== For 1
    print(f'Eu vou comer {comida}')                 ║
print('Comi pra caramba!')                          ╝
                                                        O for 1 é bom para quando souber os elemntos o 2 é para quando não souber ou for mtos
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')   ╗
for cont in range(0, len(lanche)):                                  ╠== For 2
    print(f'Eu vou comer {lanche[cont]}')                           ║
print('Comi pra caramba!')                                          ╝

NO FOR 2 É POSSIVEL MOSTRAR A POSSIÇÃO DO ELEMENTO, NO 1 NÃO
                    ↓↓↓↓
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} NA POSIÇÃO {cont}')
print('Comi pra caramba!')

Para fazer mostrar a posição no primeiro FOR 1:
                ↓↓↓↓↓
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche)) # Sorted == Colocar em ordem

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a  # Muda a ordem
print(c)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(len(c))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5)) # Quantas vezes aparece o nuemro 5 em C

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(8)) # → Em que posição está o 8?

O index nos retorna apenas a primeira ocorrencia, ou seja, o primeiro 5 ou 2 que aparecer
é o que ele irá retornar.

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(2, 4)) # Quero saber do 2 a partir da posição 4

Em outras linguagens não é possivel colocar letras e numeros na mesma tupla
no python é!

pessoa = ('Davi', 20, 'M', 78.9)
print(pessoa)

com o programa sendo exectado não é possivel alterar a tupla, mas é possivel apaga-lá
pessoa = ('Davi', 20, 'M', 78.9)
del(pessoa)
print(pessoa)

não posso deletar apenas um item
pessoa = ('Davi', 20, 'M', 78.9)
del(pessoa[0])
print(pessoa)

"""


