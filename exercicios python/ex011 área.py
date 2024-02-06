#Leia os dados de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la
lar = float(input('Qual a medida da largura da parede em metros? '))
comp = float(input('Qual a medida do comprimento da parede em metros? '))
area = lar * comp
tinta = area / 2
print('A parede tem uma área de {}m2 e irá precisar de {}l de tinta'.format(area, tinta))