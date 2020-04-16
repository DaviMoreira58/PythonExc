'''
                                        TRABALHANDO COM CORES NO TERMINAL

Padrão ANSI é um padrão de normalização internacional e dentro dele tem:
    Escape Sequence
       \033[m                                   #Sempre que quiser representar um cor no python começa com (alt+92) \033[m

entre o '\033[' e o 'm' vamos colocar os códigos de cores, que podem ser zero códigos, um código, dois códigos ou tres códigos, no exemplo ilustra 3 cóigos:
                1ºstyle       3ºback            1º Comportamento;Estilo         (normal, negrito, sublinhada)   ╗
                \033[__; __; __ m               2º Texto                        (Qual é a cor do texto)         ╠ Não importa a ordem, pq exixte diferenciação numerica entre eles
                       2ºtext                   3º Background;Cor de fundo      (Qual é a cor do fundo)         ╝
                \033[0;33;44m
                                        TABELA PADRÃO ANSI DE CORES
╔═══════════════════════════════════════════════════╦═══════════════════════════════════════╦════════════════════╗
║                    STYLE                          ║                TEXT                   ║         BACK       ║
║ 0 None - Sem estilo                               ║ 30 = Branco                           ║ 40 = Branco        ║
║ 1 Bold - Negrito                                  ║ 31 = Vermelho                         ║ 41 = Vermelho      ║
║ 4 Underline - Sublinhado                          ║ 32 = Verde                            ║ 42 = Verde         ║
║ 7 Negative - a letra vira fundo e vise-versa      ║ 33 = Amarelo                          ║ 43 = Amarelo       ║
║                                                   ║ 34 = Azul                             ║ 44 = Azul          ║
║                                                   ║ 35 = Majenta(roxo)                    ║ 45 = Majenta       ║
║                                                   ║ 36 = Ciano                            ║ 46 = Ciano         ║
║                                                   ║ 37 = Cinza                            ║ 47 = Cinza         ║
╚═══════════════════════════════════════════════════╩═══════════════════════════════════════╩════════════════════╝

{Letra branca fundo vermelho} \033[0;30;40m
{Letra amarela sublinhada funco azul} \033[4;33;44m
{Letra roxa negrito fundo amarelo} \033[1;35;43m
{Letra branca e fundo verde} \033;42m
{Letra zinza fundo preto} \033[m # config padrão
{Letra preta fundo branco} \033[7;30m


                    EXERCICIOS

print('\033[31mOlá, Mundo!') # Tudo vermelho                          ╗
print('\033[31;43mOlá, Mundo!') # Letra vermelha fundo amarelo        ╠ A faixa amarela pega tudo
print('\033[1;31;43mOlá, Mundo!') # Letra em negrito fundo amarelo    ╝
print('\033[1;31;43mOlá, Mundo!\033[m')                               = Delimita o fundo aos caracteres
print('\033[4;31;43mOlá, Mundo!\[m') # Sublinhado letra branca e fundo lilas
print('\033[30mOlá, Mundo!\033[m') # Letra branca fundo padrão(preto)
print('\03[7;30mOlá, Mundo!\033[m') # Letra preta fundo branco
print('\033[0;33;44mOlá, Mundo!\[m') # sem formatação Letra amarela fundo azul
print('\033[7;33;44mOlá, Mundo!\m') # inversor Letra azul fundo amarelo

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))
print('Os valores são \033[32;44m{}\033[m e \033[31;44m{}\033[m'.format(a, b))


nome = 'Davi'
print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
print('Olá, muito prazer em te conhecer, {}{}!!!'.format('\033[4;34m', nome)),

nome = 'Davi'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('cores['amarelo'], nome, cores['limpa']'))








































'''