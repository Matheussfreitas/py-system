despesas = []
obras = []
categorias = []
orcamentos = []

def adicionar_despesas():
    descricao = input('Informe a descrição da despesa: ')
    valor = float(input('Informe o valor da despesa: '))
    categoria = input('Informe a categoria da despesa: ')

    if valor <= 0:
        print("Erro: O valor da despesa deve ser positivo.")
        return
    if categoria not in categorias:
        print(f"Erro: A categoria '{categoria}' não existe.")
        return

    despesa = {
        'descricao': descricao,
        'valor': valor,
        'categoria': categoria
    }
    despesas.append(despesa)
    print(f"Despesa '{descricao}' registrada com sucesso na categoria '{categoria}'.")


def listar_despesas():
    if not despesas:
        print('Nenhuma despesa registrada.')
    else:
        print('\n----- Lista de despesas -----')
        for i, despesa in enumerate(despesas, start=1):
            print(f"{i}. Descrição: {despesa['descricao']}, Valor: R${despesa['valor']:.2f}, Categoria: {despesa['categoria']}")
            print('-' * 30)


def adicionar_obras():
    id = input('Informe o CPF/CNPJ do cliente da obra: ')
    nome = input('Informe o nome da obra: ')
    descricao = input('Informe o descrição da obra: ')
    servico = input('Informe o serviço a ser realizado: ')
    prioridade = input('Informe a prioridade da obra: ')

    obra = {
        'cpf/cnpj': id,
        'nome': nome,
        'descricao': descricao,
        'tipo_servico': servico,
        'prioridade': prioridade
    }
    obras.append(obra)


def listar_obras():
    if not obras:
        print('Nenhuma obra registrada.')
    else:
        print('\n----- Lista de obras -----')
        for i, obra in enumerate(obras, start=1):
            print(f"{i}. CPF/CNPJ: {obra['cpf/cnpj']}, Descrição: {obra['descricao']}, Tipo de Serviço: {obra['tipo_servico']}, Prioridade: {obra['prioridade']}")
            print('-' * 30)


def criar_categorias():
    categoria = input('Informe a nova categoria: ')

    if categoria in categorias:
        print(f"Erro: Categoria '{categoria}' já existente.")
        return
    categorias.append(categoria)
    print(f"Categoria '{categoria}' criada com sucesso.")


def listar_categorias():
    if not categorias:
        print('Nenhuma categoria criada.')
        return
    else:
        print('\n----- Categorias criadas -----')
        for i, categoria in enumerate(categorias, start=1):
            num_despesas = sum(1 for despesa in despesas if despesa['categoria'] == categoria)
            print(f'{i}. {categoria} (Despesas: {num_despesas})')
            print('-' * 30)


def criar_orcamentos():
    obra = input('Informe o nome da obra: ')
    descricao = input('Informe a descrição do orçamento: ')
    orcamento = float(input('Informe o valor do orçamento: '))

    if not obra['cpf/cnpj'] in obras:
        print(f"Erro: A obra {obra} não está cadastrada.")
        return
    if obra['cpf/cnpj'] in obras:
        print(f"Erro: Obra '{obra['nome']}' já possui um orçamento.")
        return
    if orcamento <= 0:
        print("Erro: O valor do orçamento deve ser positivo.")
        return

    orcamento = {
        'obra': obra,
        'descricao': descricao,
        'valor': orcamento,
    }
    orcamentos.append(orcamento)
    print(f"Orçamento '{descricao}' criado com sucesso para a obra '{obra}', no valor de {orcamento}.")
    

def listar_orcamentos():
    if not orcamentos:
        print('Nenhum orçamento criado.')
        return
    
    print('\n----- Lista de Orçamentos -----')
    for i, orcamento in enumerate(orcamentos, start=1):
        total_despesas = sum(
            despesa['valor'] for despesa in despesas
            if despesa['categoria'] == orcamento['categoria']
        )
        saldo = orcamento['orcamento'] - total_despesas

        print(f"{i}. Descrição: {orcamento['descricao']}")
        print(f"   Categoria: {orcamento['categoria']}")
        print(f"   Orçamento: R$ {orcamento['orcamento']:.2f}")
        print(f"   Despesas: R$ {total_despesas:.2f}")
        print(f"   Saldo: R$ {saldo:.2f}")
        print('-' * 30)