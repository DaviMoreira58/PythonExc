# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses
# abertos e fechados na ordem correta.

"""abertos = []
fechados = []
a = f = 0
while True:
    parenteses = input('Digite sua expressão: ')
    while '(' in parenteses:
        a += 1
        abertos.append(a)
    while ')' in parenteses:
        f += 1
        fechados.append(f)
    if abertos == fechados:
        print('Sua expressão é valida!')
        break
    if a != f:
        print('Sua expressão é invalida!')
        break
print(fechados)
print(abertos)""" # não consegui fazer, mas foi no sentido correto

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
