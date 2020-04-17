#OPERADORES ARITIMÉTICOS

# 5+2==7 SOMA
# 5-2==3 SUBTRAÇÃO
# 5*2==10 MULTIPLICAÇÃO
# 5/2==2.5 DIVISÃO
# 5**2==25 POTENCIA
# 5//2==2 DIVISAO INTEIRA              5├²
# 5%2==1 RESTO DA DIVISAO       resto► 1|2 ◄inteira(Quociente)

#ORDE DE PRECEDENCIA
# 1° ()
# 2° **
# 3° *././/.% - Todos em 3° lugar
# 4° +.-

#EXEMPLO

# 5+3*2==11
# 3*5+4**2==31
# 3*(5+4)**2==243
# pow(4,3)==64 - é outra forma de potencia
# 81**(1/2)==9 - raiz quadrada

#CURIOSIDADES

# 'Oi'+ 'Olá' == 'OiOlá'
# 'Oi'*5 ==OiOiOiOiOi
# '='*20 == '===================='
# print('='*20) == ==================== fica sem as aspas

#Exc aula

nome = str(input('Qual é o seu nome? '))
print('Prazer em te conhecer {:=^20}!'.format(nome)) #":"Faz Davi aparecer em 20 caracteres e ">" alinha a direita "<" alinhado a esquerda "^" centraliza e qualquer caracter antes como "=" será preenchido nos espaços

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2)) # Não usamos a variavel porque não iremos precisar desse valor depois, caso precisemos é só acrescentar
print('A multiplicação vale {}'.format(n1*n2))
print('O resto da divisão vale {}'.format(n1%n2))
#OUTRAS MANEIRAS

n3 = int(input('Terceiro valor: '))
n4 = int(input('Quarto valor: '))
s = n3 + n4
m = n3 * n4
d = n3 / n4
di = n3 // n4
e = n3 ** n4
print('A soma é {} a multiplicão é {} e a divisão é {:.3f}'.format(s, m, d)) #Esse":.3f" é para limitar a divisão a tres pontos flutuantes
print('O resto é {} a potencia é {}'.format(di, e))
# , end=' ' - para juntas os prints,pode preencher o espaço vazio ", end='>>>'" e \n para quebrar no meio
