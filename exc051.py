# Desenvolva um programa que leia o primeiro termo e a razao de uma PA. no final
# mostre os 10 primeiros termos dessa progressão

'''i = int(input('Início: '))  # numero inicial
p = int(input('Passo: '))   # intervalo de "Pulo"
f = range[0, 10]

print(f)
print('FIM')''' # Erro

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='→ ')
print('Acabou')
