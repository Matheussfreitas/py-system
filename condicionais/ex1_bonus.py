vendas01 = float(input("Qual o valor de suas vendas? "))
vendas02 = float(input("Qual o valor de suas vendas? "))
vendas03 = float(input("Qual o valor de suas vendas? "))
meta = int (1000)

if vendas01 >= meta:
    bonus = vendas01 * 0.1
    print(f"O bônus do funcionario 1 é de {bonus}")
else:
    print("O funcionario não recebe bônus.")

if vendas02 >= meta:
    bonus = vendas02 * 0.1
    print(f"O bônus do funcionario 2 é de {bonus}")
else:
    print("O funcionario não recebe bônus.")

if vendas03 >= meta:
    bonus = vendas03 * 0.1
    print(f"O bônus do funcionario 3 é de {bonus}")
else:
    print("O funcionario não recebe bônus.")



