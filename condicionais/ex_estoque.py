nome_produto = input("Qual o nome do produto? ")
categoria_produto = input("Qual a categoria do produto? ")
quantidade_produto = int(input("Qual a quantidade do produto? "))

if categoria_produto and nome_produto and quantidade_produto:
    if categoria_produto == "limpeza":
        if quantidade_produto < 30:
            print(f"Solicitar {nome_produto} à equipe de compras, temos apenas {quantidade_produto} no estoque")
    elif categoria_produto == "bebidas":
        if quantidade_produto < 75:
            print(f"Solicitar {nome_produto} à equipe de compras, temos apenas {quantidade_produto} no estoque")
    elif categoria_produto == "alimentos":
        if quantidade_produto < 50:
            print(f"Solicitar {nome_produto} à equipe de compras, temos apenas {quantidade_produto} no estoque")
else:
    print("Preencha todas as informações.")