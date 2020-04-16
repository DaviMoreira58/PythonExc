#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area
# e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2 m²

#n1 = int(input('Qual a altura da parede? '))
#n2 = int(input('Qual é a largura? '))
#n3 = n1 * n2
#n4 = n3 / 2
#print('A quantidade de tinta que será utilizada é de {} litros'.format(n4))

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}m x {}m e sua area é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))

