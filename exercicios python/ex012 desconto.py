#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com % de desconto
preço = float(input('Qual o valor do produto? R$ '))
desconto = int(input('Qual a porcentagem do desconto? '))
preço_final = preço * desconto / 100
print('O novo valor com {}% de desconto é de {:.2f}R$'.format(desconto, preço_final))