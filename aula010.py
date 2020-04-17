# CONDIÇOES SIMPLES E COMPOSTAS
'''
╔════ Exemplo: Controlando um carro com um unico caminho
║ carro.siga()
║ carro.esquerda()
║ carro.siga()
║ carro.direita()
║ carro.siga()
║ carro.direita()
║ carro.siga()
║ carro.esquerda()
║ carro.siga()
║ carro.pare()
║
▼
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

╔══════ Exemplo: Controlando um carro com duas possilidades
║             iremos utilizar a funçao se e senão
╚═══════════════════════════╗
                            ▼
╔ carro.esquerda() ▓ ◄ carro.siga() ► ▓ ╗ carro.direita()
║ carro.siga()                          ║ carro.siga()
║ carro.direita()                       ║ carro.esquerda()
║ carro.siga()                          ║ carro.siga()
║ carro.direita()                       ║ carro.esquerda()
║ carro.esquerda()                      ║ carro.siga()
║ carro.siga()                          ║ carro.pare()
║ carro.direita()                       ║
║ carro.siga()                          ║
╚══════════ ►      ▓  carro.pare()   ▓ ◄╝
                           ║
                           ║
                           ▼

carro.siga()
se carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()                         identação
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
senão
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
carro.pare()

#ESTRUTURA CONDICIONAL

se carro.esquerda()   ►   if carro.esquerda():
    bloco_V_          ►       bloco True
senão                 ►   else:
    bloco_F_          ►       bloco False


tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

# outra maneira
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo<=3 else'carro velho')
print('--FIM--')
'''

'''
# EXERCICIOS AULA

nome = str(input('Qual é o seu nome? '))
if nome == 'Davi':
    print('Que nome lindo que você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n1)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('sua média foi boa, parabens por fazer o minimo')
else:
    print('Sua média foi um lixo igual você! Parabens!!')
# print('PARABENS' if m >= 6 else 'ESTUDE MAIS!') #IF simplificado









'''
