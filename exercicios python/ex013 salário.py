#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Qual o valor do seu salário? R$'))
aumento = int(input('Qual a % de aumento? '))
novo_salario = salario + (salario * aumento/100)
print('O novo salário é de {:.2f}R$ com aumento de {}%'.format(novo_salario, aumento))
