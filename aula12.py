'''
                            CONDIÇÕES ANINHADAS

VEJA A AULA 10 QUE ESTÁ ILUSTRADO, NESSE EXEMPLO TEM TRES CAMINHOS RETO, ESQ, DIR

carro.siga()                        »carro.siga()
se carro.esquerda()                 »if carro.esquerda():
    carro.siga()                    »   carro.siga()
    carro.direita()                 »   carro.direita()
    carro.siga()                    »   carro.siga()
    carro.direita()                 »   carro.direita()
    carro.esquerda()                »   carro.esquerda()
    carro.siga()                    »   carro.siga()
senão se carro.direita()            »elif carro.direita():
    carro.siga()                    »   carro.siga()
    carro.esquerda()                »   carro.esquerda()
    carro.siga()                    »   carro.siga()
    carro.esquerda()                »   carro.esquerda()
    carro.siga()                    »   carro.siga()
senão                               »else:
    carro.siga()                    »   carro.siga()
carro.pare()                        »carro.pare()

                    PRATICA

nome = str(input('Qual é o seu nome? '))
if nome == 'Davi':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é tão comum!')
print('Tenha um bom dia, {}!'.format(nome))
'''
