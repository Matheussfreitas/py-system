# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
metros = float(input('Digite o valor em metros: '))
cent = metros * 100
mil = metros * 1000
print('O valor de {} metros em centímetros é {} e em milimímetros é {}'.format(metros, cent, mil))