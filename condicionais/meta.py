meta = float(input("Qual o valor da sua meta? "))
vendas = float(input("Qual foi o valor das suas vendas? "))

if vendas > meta * 2:
    bonus = vendas * 1.07
    print(f"O seu bônus foi 7%, com valor de {bonus}")
elif vendas > meta:
    bonus = vendas * 1.03
    print(f"O ser bônus foi de 3%, com valor de {bonus}")
else:
    print("Você não tem direito a bônus")