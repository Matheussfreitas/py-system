#Faça um programa que leia a quantidade de Km rodados pelo carro alugado e a quantidade de dias que foi alugado
km = float(input('Qual a quantidade de km rodados pelo carro? '))
dia = int(input('Informe a quantidade de dias? '))
preço_dia = dia * 60
preço_km = km * 0.15
preço_final = preço_dia + preço_km
print('O valor por km é {:.2f}R$ e por dia é {:.2f}R$, o valor total é de {:.2f}R$'.format(preço_km, preço_dia, preço_final))