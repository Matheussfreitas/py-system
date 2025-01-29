despesas = []
categorias = []
orcamentos = []

def adicionar_despesas(descricao, valor, categoria):
    despesas.append(f'Descrição: {descricao}, Valor: R${valor:.2f}, Categoria: {categoria}')
    print('Despesa registrada com sucesso.')
    return despesas

def listar_despesas():
    if not despesas:
        print('Nenhuma despesa registrada.')
    else:
        for i, despesa in enumerate(despesas):
            print('----- Lista de despesas -----\n')
            print(f'{i + 1}. {despesa}')

            print('-' * 30)

def criar_categorias(categoria):
    categorias.append(categoria)
    print('Categoria criada com sucesso.')
    return categorias

def listar_categorias():
    if not categorias:
        print('Nenhuma categoria criada.')
    else:
        print('----- Categorias criadas -----\n')
        for i, categoria in enumerate(categorias):
            print(f'{i + 1}. {categoria}')
            print('-' * 30)

def criar_orcamentos(categoria, orcamento, descricao):
    if categoria not in categorias:
        print('Categoria inexistente.')
    else:
        orcamentos.append(f'Descrição: {descricao}, Categoria: {categoria}, Valor: R${orcamento:.2f}')
        print('Orçamento criado com sucesso.')
        return orcamentos
    
def listar_orcamentos():
    if not orcamentos:
        print('Nenhum orçamento criado.')
    else:
        for i, orcamento in enumerate(orcamentos):
            print('Lista de orçamentos criados:\n')
            print(f'{i + 1}. {orcamento}')