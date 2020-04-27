"""
                        VARIAVEIS COMPOSTAS
                             LISTAS
                            (parte 2)
    (PARTE 1)
        dados = list()
        dados.append('Davi')
        dados. append(25)
        print(dados[0]) → 'Davi'
        print(dados[1]) → '25'

    (PARTE 2)
        dados = list()
        dados.append('Davi')
        dados.append(25)
        print(dados[0]) → 'Davi'
        print(dados[1]) → '25'
        -=-=-=-=-=-=-=-=-=-=-=-=
        pessoas = list()
        pessoas.append(dados[:]) → Isso faz com que a lista tenah outra lista dentro dela

                   LISTA PESSOAS ↓↓
        ___________________________________________________________
        │                   LISTA DADOS:                          │
        │▬▬▬▬▬▬▬  │ ▬▬▬▬▬▬▬▬▬ │ ▬▬▬▬▬▬▬▬▬▬▬   │
        │█'Davi'█ 25 █ │ █ 'Maria' █ 30 █ │  █ 'Antonio' █  22 █  │
        │█  0   █ 1  █ │ █   0     █  1 █ │  █     1     █   0 █  │
        │▬▬▬▬▬▬▬  │ ▬▬▬▬▬▬▬▬▬ │ ▬▬▬▬▬▬▬▬▬▬▬   │
        -----------------------------------------------------------
        │        0      │        1        │            2          │

pessoas = [['Davi', 25], ['Maria', 30], ['Antonio', 22]]

print(pessoas[0][0]) → Davi
print(pessoas[1][1]) → 30
print(pessoas[2][0]) → Antonio
print(pessoas[1]) → ['Maria', 30]

                Pratica:

teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
print(galera)

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera) #[['Maria', 22], ['Maria', 22]]

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # Copiou
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) # Copiou
print(galera) # → [['Gustavo', 40], ['Maria', 22]]

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera) # → [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0]) # → ['João', 19]

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0]) # → João

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1]) # → 13

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p) # → ['João', 19]
             # → ['Ana', 33]
             # → ['Joaquim', 13]
             # → ['Maria', 45]

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[0]) # → João
                # → Ana
                # → Joaquim
                # → Maria

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[1]) # → 19
                # → 33
                # → 13
                # → 45

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade') # → João tem 19 anos de idade
                                              # → Ana tem 33 anos de idade
                                              # → Joaquim tem 13 anos de idade
                                              # → Maria tem 45 anos de idade

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # Se não utilizar os ':', a cópia, nesse caso irá gerar
    dado.clear() # listas vazias por causa desse 'clear'
print(galera)

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade.')


"""


