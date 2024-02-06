# Crie um programa que leia quanto dinheiro uma pessoa tem e mostre quantos dólares ela pode comprar.
real = float(input('Qual o valor que tem em sua carteira? R$ '))
dolar = 5.05 
conversao = real / dolar
print('Você pode comprar {:.2f} U$ com {:.2f} R$'.format(conversao, real))