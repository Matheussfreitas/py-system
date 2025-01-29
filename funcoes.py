despesas = []

def adicionar_despesas (descricao, valor, categoria):
    despesas.append(f'Descrição: {descricao}, Valor: R${valor:.2f}, Categoria: {categoria}')
    print('Despesa registrada com sucesso.')
    return despesas

def listar_despesas():
    if not despesas:
        print('Nenhuma despesa registrada.')
    else:
        for i, despesa in enumerate(despesas):
            print('Lista de despesas registradas:\n')
            print(f'{i + 1}. {despesa}')