import funcoes

menu = """
             ********** MENU **********

             1. Cadastrar despesa
             2. Consultar despesas avulsas
             3. Cadastrar obra
             4. Consultar obras
             5. Criar categorias
             6. Consultar categorias
             7. Criar orçamentos
             8. Consultar orçamentos
             9. Sair

             **************************
    """

numeroControle = -1

while numeroControle != 0:
    print(menu)
    numeroControle = int(input('Digite o número da opção desejada: '))

    if numeroControle == 1:
        funcoes.adicionar_despesas()

    elif numeroControle == 2:
        funcoes.listar_despesas()

    elif numeroControle == 3:
        funcoes.adicionar_obras()

    elif numeroControle == 4:
        funcoes.listar_obras()

    elif numeroControle == 5:
        funcoes.criar_categorias()

    elif numeroControle == 6:
        funcoes.listar_categorias()

    elif numeroControle == 7:
        funcoes.criar_orcamentos()

    elif numeroControle == 8:
        funcoes.listar_orcamentos()

    elif numeroControle == 9:
        print('Programa encerrado.')
        numeroControle = 0