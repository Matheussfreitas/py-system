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
             9. Atualizar status da obra
             10. Relatório financeiro por obra
             11. Listar obras atrasadas
             12. Sair

             **************************
    """

opcao = -1

while opcao != 0:
    print(menu)
    opcao = int(input('Digite o número da opção desejada: '))

    if opcao == 1:
        funcoes.adicionar_despesas()
    elif opcao == 2:
        funcoes.listar_despesas()
    elif opcao == 3:
        funcoes.adicionar_obras()
    elif opcao == 4:
        funcoes.listar_obras()
    elif opcao == 5:
        funcoes.criar_categorias()
    elif opcao == 6:
        funcoes.listar_categorias()
    elif opcao == 7:
        funcoes.criar_orcamentos()
    elif opcao == 8:
        funcoes.listar_orcamentos()
    elif opcao == '9':
        funcoes.atualizar_status_obra()
    elif opcao == '10':
        funcoes.relatorio_financeiro_obra()
    elif opcao == '11':
        funcoes.listar_obras_atrasadas()
    elif opcao == '12':
        print('Saindo do sistema...')
        opcao = 0
    else:
        print('Opção inválida. Tente novamente.')