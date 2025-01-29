import funcoes

menu = """
             ********** MENU **********

             1. Registrar despesas
             2. Consultar despesas
             3. Sair

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
        print('Programa encerrado.')
        numeroControle = 0