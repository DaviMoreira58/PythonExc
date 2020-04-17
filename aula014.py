'''
                        Estruturas de laços
                                WHILE
    #ESTRUTURA DE REPERIÇÃO COM TESTE LÓGICO (WHILE)
O exemplo é do personagem que nçao sabe quantos passos tem até a maça

enquanto não (maça)     while not maça         não chegou na maça
    passo                   passo              continua andando
pega                    pega                   chegou, então pega a (maça)

o Exemplo é do personagem com um caminho todo irregular(com buracos aleatorios) e moedas

enquanto não maça       while not maça:
    se tem chão             if chão:
        passo                   passo
    se tiver buraco         if buraco:
        pula                    pulo
    se tiver moeda          if moeda:
        pega                    pega
pega                    pega

Exercicos
Contador com FOR:
for c in range(1, 10):
    print(c)
print('Fim')
Contador com WHILE:
c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')

Nesse caso sabemos quantas vezes o programa vai rodar:
for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')

Nesse caso não sabemos quanrtas vezes o programa vai rodar:
n = 1
while n != 0: # "n != 0" é chamado de Flag, ponto de parada!
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} numeros pares e {} numeros impares'.format(par, impar))






































'''