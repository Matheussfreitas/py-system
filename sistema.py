import funcoes

menu = """
             ********** MENU **********

             1. Registrar despesas avulsas
             2. Consultar despesas avulsas
             3. Criar categorias
             4. Consultar categorias
             5. Criar orçamentos
             6. Consultar orçamentos
             7. Sair

             **************************
    """

numeroControle = -1

while numeroControle != 0:
    print(menu)
    numeroControle = int(input('Digite o número da opção desejada: '))

    if numeroControle == 1:
        descricao = input('Informe a descrição da despesa: ')
        valor = float(input('Informe o valor da despesa: '))
        categoria = input('Informe a categoria da despesa: ')
        funcoes.adicionar_despesas(descricao, valor, categoria)
    elif numeroControle == 2:
        funcoes.listar_despesas()
    elif numeroControle == 3:
        categoria = input('Informe a nova categoria: ')
        funcoes.criar_categorias(categoria)
    elif numeroControle == 4:
        funcoes.listar_categorias()
    elif numeroControle == 5:
        categoria = input('Informe a categoria do orçamento: ')
        orcamento = float(input('Informe o valor do orçamento: '))
        descricao = input('Informe a descrição do orçamento: ')
        funcoes.criar_orcamentos(categoria, orcamento, descricao)
    elif numeroControle == 6:
        funcoes.listar_orcamentos()
    elif numeroControle == 7:
        print('Programa encerrado.')
        numeroControle = 0