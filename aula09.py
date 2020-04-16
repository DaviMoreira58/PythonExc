# Manipulando cadeias de texto
# Frase base: Curso me video python - tem 21 caracteres com os espaços
# Fatiamento:
''' FRASE = Curso em video python (21 CARCTERES)
C u r s o   e m   V  í  d  e  o     P  y  t  h  o  n
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
'''
# Exp: frase[9] - o conchete é um identificador de estrutura chamada lista
# Se fizermos print(frase[9]) esse '9' irá limitar até o caracter 9 , seria:
# "curso em v"
# print(frase[9:13]) - vai de 9 até 12. no inicio começa com o caracter que vc quer, o final sempre sera -1
# "vide"
# print(frase[9:21]) não é o ideal
# "video python"
# print(frase[9:21:2] - vai pulando de duas em duas casa
# "Vdopto"
# print(frase[:5] - quando não determinamos o inicio, por padrão começa no 0
# "curso"
# print(frase[15:]) - indicamos apenas o começo, entao ele vai até o final
# "Python"
# print(frase[9::3]) - não indicamos o final, então começa no 9 e vai pulando 3
# "Veph"

# ANALISE
# primeira funçao "len". Vem de lens, significa comprimento, basicamente ele mostra quanto caracteres tem a frase, no nosso caso tem 21
'''len(frase)'''
# segunda funçao "count"
# frase.count('o') - pede para o programa contar quantas vezes a letra 'o' minuscula aparece
# frase.count('o', 0, 13) - vai fazer uma contagem de 'o' do zero ao treze, lembrando que ele "lê" até o 12
# terceira funçao "find"
# frase.find('deo') - pede para procurar na frase em que momento começou o "deo", no nosso caso no 11
# frase.find('Android') - quando colocamos uma string que nao existe, o programa retorna "-1"
# 'Curso' in frase - podemos usar o "in", seria "Exixte a palavra 'Curso' na 'frase'?". nos retorna True ou False não é uma funçao, sim um operador
# True

# TRANSFORMAÇÃO
'''Via de regra uma lista de string é imutavel, não conseguimos alterar ela(elementos), porem conseguimos mudar ela através dos métodos'''
# print(frase.replace('Python, 'Android')) - replece é trocar, substituir
# Curso em Video Android
# frase.upper() - upper é "pra cima", deixe maiusculo. é obrigatorio o (), pois upper é um método
# "CURSO EM VIDEO PYTHON" - deixou tudo maiusculo
# frase.lower() - lower poe tudo em minusculo
# "curso em video python"
# frase.capitalize() - vai jogar todos os caracteres para minusculo e deixar apenas o primeiro maisculo
# "Curso em video python"
# frase.title() - parece com o 'capitalize', mais faz uma analise mais profunda, analisa quantas palavras tem na frase(4), faz essa analise onde a espaços e faz o 'capitalize' palavra por palavra
# "Curso Em Vídeo Python"

'''Frase = 18 caracteres
      A p r e n d a    P  y  t  h  o  n
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18'''
# frase.stip() - remove todos os espaçoes inuteis no inicio e final da string
'''
A p r e n d a   P y t h o n
0 1 2 3 4 5 6 7 8 9 10 11 12 '''
# frase.rstrip() - algumas funcionalidades do python utilizam o "r" para tratar stings, ele remove somente os ultimos espaços
# frase.lstrip() - remove os espaços da esquerda e mantem os da direita

#DIVISÃO
''' FRASE = Curso em video python (21 CARCTERES)
C u r s o   e m   V  í  d  e  o     P  y  t  h  o  n
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
'''
# frase.split() - 'tem funçoes no parenteses a mais' o split cia um divisão onde tem espaços

''' FRASE = Curso em Vídeo Python
░ C u r s o ░  e m  ░  V  í  d  e  o  ░   P  y  t  h  o  n ░    Palavra 1 = Curso ; Palavra 2 = em
░ 0 1 2 3 4 ░  0 1  ░  0  1  2  3  4  ░   0  1  2  3  4  5 ░    Palavra 3 = Video ; Palavra 4 = Python
      0         1             2                  3
'''
#JUNÇÃO

''' FRASE = Curso em Vídeo Python
░ C u r s o ░  e m  ░  V  í  d  e  o  ░   P  y  t  h  o  n ░    Palavra 1 = Curso ; Palavra 2 = em
░ 0 1 2 3 4 ░  0 1  ░  0  1  2  3  4  ░   0  1  2  3  4  5 ░    Palavra 3 = Video ; Palavra 4 = Python
      0         1             2                  3
'''
# '-'.join(frase) - significa que ele vai juntar todos os elementos da frase (0,1,2,3) e usar '-' para separar
''' FRASE = Curso em video python (21 CARCTERES)
C u r s o - e m - V  í  d  e  o  -  P  y  t  h  o  n # caso queira colocar um espaço é só deixar em branco ► ' '.
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 '''

#EXERCICIOS AULA

'''frase = 'Curso em Vídeo Python'
print(frase[3])'''
'''frase = 'Curso em Vídeo Python'
print(frase[3:13])'''
'''frase = 'Curso em Vídeo Python'
print(frase[:13])'''
'''frase = 'Curso em Vídeo Python'
print(frase[1:15])'''
'''frase = 'Curso em Vídeo Python'
print(frase[1:15:2])'''
'''frase = 'Curso em Vídeo Python'
print(frase[1::2])'''
'''frase = 'Curso em Vídeo Python'
print(frase[::2])'''
'''print("""Nessa aula, vamos aprender operações com 
String no Python. As principais operações que vamos
aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com
replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().""")'''
'''frase = 'Curso em Vídeo Python'
print(frase.count('O'))'''
'''frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))'''
#VAMOS USAR MUITO▼▼▼▼
'''frase = 'Curso em Vídeo Python'
print(len(frase))'''
#▲▲▲▲
'''frase = '   Curso em Vídeo Python    '
print(len(frase.strip()))'''
'''frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))'''
'''frase = 'Curso em Vídeo Python'
frase.replace('Python', 'Android')
print(frase)'''
'''frase = 'Curso em Vídeo Python'
frase = frase.replace('Python', 'Android')
print(frase)'''
'''frase = 'Curso em Vídeo Python'
print('Curso' in frase)'''
'''frase = 'Curso em Vídeo Python'
print(frase.find('Curso'))'''
'''frase = 'Curso em Vídeo Python'
print(frase.find('Vídeo'))'''
'''frase = 'Curso em Vídeo Python'
print(frase.find('video'))'''
'''frase = 'Curso em Vídeo Python'
print(frase.lower().find('vídeo'))'''
'''frase = 'Curso em Vídeo Python'
print(frase.split())'''
'''frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido)'''
'''frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0])'''
'''frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[2][3])'''

