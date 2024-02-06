funcionario = float(input("Qual a quantidade de suas vendas? "))

if funcionario >= 2000:
    bonus = funcionario * 0.15
elif funcionario >= 1000:
    bonus = funcionario * 0.1
else:
    bonus = 0
print(f"O bônus do funcionario é de {bonus}R$")