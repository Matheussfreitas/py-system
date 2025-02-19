despesas = []
obras = []
categorias = []
orcamentos = []

from datetime import datetime

def adicionar_despesas():
    descricao = input('Informe a descrição da despesa: ')
    valor = float(input('Informe o valor da despesa: '))
    categoria = input('Informe a categoria da despesa: ')
    obra_cpf_cnpj = input('Informe o CPF/CNPJ da obra associada (deixe em branco se não houver): ').strip()

    if valor <= 0:
        print("Erro: O valor da despesa deve ser positivo.")
        return
    if categoria not in categorias:
        print(f"Erro: A categoria '{categoria}' não existe.")
        return

    obra_associada = None
    if obra_cpf_cnpj:
        for obra in obras:
            if obra['cpf_cnpj'] == obra_cpf_cnpj:
                obra_associada = obra_cpf_cnpj
                break
        if not obra_associada:
            print(f"Erro: Obra com CPF/CNPJ '{obra_cpf_cnpj}' não encontrada.")
            return

    despesa = {
        'descricao': descricao,
        'valor': valor,
        'categoria': categoria,
        'obra': obra_associada
    }
    despesas.append(despesa)
    print(f"Despesa '{descricao}' registrada com sucesso na categoria '{categoria}'." + (f" Associada à obra {obra_cpf_cnpj}." if obra_associada else ""))

def listar_despesas():
    if not despesas:
        print('Nenhuma despesa registrada.')
    else:
        print('\n----- Lista de Despesas -----')
        for i, despesa in enumerate(despesas, start=1):
            obra_str = f", Obra: {despesa['obra']}" if despesa['obra'] else ""
            print(f"{i}. Descrição: {despesa['descricao']}, Valor: R${despesa['valor']:.2f}, Categoria: {despesa['categoria']}{obra_str}")
            print('-' * 30)

def adicionar_obras():
    id = input('Informe o CPF/CNPJ do cliente da obra: ')
    nome = input('Informe o nome da obra: ')
    descricao = input('Informe a descrição da obra: ')
    servico = input('Informe o serviço a ser realizado: ')
    prioridade = input('Informe a prioridade da obra: ')
    data_inicio = input('Informe a data de início (DD/MM/AAAA): ')
    data_prevista = input('Informe a data prevista de término (DD/MM/AAAA): ')
    status = input('Informe o status (Planejada/Em andamento/Concluída/Atrasada): ').capitalize()

    opcoes_status = ['Planejada', 'Em andamento', 'Concluída', 'Atrasada']
    if status not in opcoes_status:
        print("Erro: Status inválido. Use uma das opções: Planejada, Em andamento, Concluída, Atrasada.")
        return

    try:
        datetime.strptime(data_inicio, '%d/%m/%Y')
        datetime.strptime(data_prevista, '%d/%m/%Y')
    except ValueError:
        print("Erro: Data no formato inválido. Use DD/MM/AAAA.")
        return

    for obra in obras:
        if obra['cpf_cnpj'] == id:
            print(f"Erro: Obra com o CPF/CNPJ '{id}' já registrada.")
            return

    obra = {
        'cpf_cnpj': id,
        'nome': nome,
        'descricao': descricao,
        'tipo_servico': servico,
        'prioridade': prioridade,
        'data_inicio': data_inicio,
        'data_prevista': data_prevista,
        'status': status
    }
    obras.append(obra)
    print(f"Obra '{nome}' cadastrada com sucesso.")

def listar_obras():
    if not obras:
        print('Nenhuma obra registrada.')
    else:
        print('\n----- Lista de Obras -----')
        for i, obra in enumerate(obras, start=1):
            print(f"{i}. CPF/CNPJ: {obra['cpf_cnpj']}, Nome: {obra['nome']}")
            print(f"   Descrição: {obra['descricao']}, Serviço: {obra['tipo_servico']}")
            print(f"   Prioridade: {obra['prioridade']}, Status: {obra['status']}")
            print(f"   Data Início: {obra['data_inicio']}, Previsão Término: {obra['data_prevista']}")
            print('-' * 30)

def criar_categorias():
    categoria = input('Informe a nova categoria: ').strip()
    
    if not categoria:
        print("Erro: A categoria não pode ser vazia.")
        return    
    if categoria in categorias:
        print(f"Erro: Categoria '{categoria}' já existente.")
        return
    categorias.append(categoria)
    print(f"Categoria '{categoria}' criada com sucesso.")

def listar_categorias():
    if not categorias:
        print('Nenhuma categoria criada.')
    else:
        print('\n----- Categorias Criadas -----')
        for i, categoria in enumerate(categorias, start=1):
            num_despesas = sum(1 for despesa in despesas if despesa['categoria'] == categoria)
            print(f'{i}. {categoria} (Despesas: {num_despesas})')
            print('-' * 30)

def criar_orcamentos():
    cpf_cnpj = input('Informe o CPF/CNPJ da obra: ')

    obra_existente = None
    for obra in obras:
        if obra['cpf_cnpj'] == cpf_cnpj:
            obra_existente = obra
            break

    if not obra_existente:
        print(f"Erro: A obra com CPF/CNPJ '{cpf_cnpj}' não está cadastrada.")
        return
    
    descricao = input('Informe a descrição do orçamento: ')
    valor = float(input('Informe o valor do orçamento: '))

    if valor <= 0:
        print("Erro: O valor do orçamento deve ser positivo.")
        return

    orcamento = {
        'obra': cpf_cnpj,
        'descricao': descricao,
        'valor': valor,
    }
    orcamentos.append(orcamento)
    print(f"Orçamento '{descricao}' criado com sucesso para a obra '{obra_existente['nome']}'.")

def listar_orcamentos():
    if not orcamentos:
        print('Nenhum orçamento criado.')
        return
    
    orcamentos_por_obra = {}
    for orcamento in orcamentos:
        chave = orcamento['obra']
        if chave not in orcamentos_por_obra:
            orcamentos_por_obra[chave] = []
        orcamentos_por_obra[chave].append(orcamento)
    
    print('\n----- Lista de Orçamentos por Obra -----')
    for obra_cpf in orcamentos_por_obra:
        nome_obra = "Não encontrado"
        for obra in obras:
            if obra['cpf_cnpj'] == obra_cpf:
                nome_obra = obra['nome']
                break
        
        total_obra = sum(o['valor'] for o in orcamentos_por_obra[obra_cpf])
        print(f"Obra: {nome_obra} ({obra_cpf}) - Total Orçado: R$ {total_obra:.2f}")
        for i, orcamento in enumerate(orcamentos_por_obra[obra_cpf], start=1):
            print(f"  {i}. Descrição: {orcamento['descricao']}, Valor: R$ {orcamento['valor']:.2f}")
        print('-' * 30)

def atualizar_status_obra():
    cpf_cnpj = input('Informe o CPF/CNPJ da obra: ')
    novo_status = input('Novo status (Planejada/Em andamento/Concluída/Atrasada): ').capitalize()
    
    opcoes_status = ['Planejada', 'Em andamento', 'Concluída', 'Atrasada']
    if novo_status not in opcoes_status:
        print("Erro: Status inválido.")
        return
    
    for obra in obras:
        if obra['cpf_cnpj'] == cpf_cnpj:
            obra['status'] = novo_status
            print(f"Status da obra '{obra['nome']}' atualizado para '{novo_status}'.")
            return
    print(f"Obra com CPF/CNPJ {cpf_cnpj} não encontrada.")

def relatorio_financeiro_obra():
    cpf_cnpj = input('Informe o CPF/CNPJ da obra para gerar relatório: ')
    
    obra_encontrada = None
    for obra in obras:
        if obra['cpf_cnpj'] == cpf_cnpj:
            obra_encontrada = obra
            break
    if not obra_encontrada:
        print(f"Obra com CPF/CNPJ {cpf_cnpj} não encontrada.")
        return
    
    total_orcado = sum(orcamento['valor'] for orcamento in orcamentos if orcamento['obra'] == cpf_cnpj)
    total_despesas = sum(despesa['valor'] for despesa in despesas if despesa.get('obra') == cpf_cnpj)
    
    lucro = total_orcado - total_despesas
    margem = (lucro / total_orcado * 100) if total_orcado != 0 else 0.0
    
    print(f"\nRelatório Financeiro para Obra: {obra_encontrada['nome']}")
    print(f"CPF/CNPJ: {cpf_cnpj}")
    print(f"Total Orçado: R$ {total_orcado:.2f}")
    print(f"Total de Despesas: R$ {total_despesas:.2f}")
    print(f"Lucro: R$ {lucro:.2f}")
    print(f"Margem de Lucro: {margem:.2f}%")

def listar_obras_atrasadas():
    hoje = datetime.now().date()
    obras_atrasadas = []
    
    for obra in obras:
        try:
            data_prevista = datetime.strptime(obra['data_prevista'], '%d/%m/%Y').date()
            if data_prevista < hoje and obra['status'] != 'Concluída':
                obras_atrasadas.append(obra)
        except:
            continue
    
    if not obras_atrasadas:
        print('Nenhuma obra atrasada encontrada.')
        return
    
    print('\n----- Obras Atrasadas -----')
    for i, obra in enumerate(obras_atrasadas, start=1):
        print(f"{i}. Nome: {obra['nome']}, CPF/CNPJ: {obra['cpf_cnpj']}")
        print(f"   Data Prevista: {obra['data_prevista']}, Status: {obra['status']}")
        print('-' * 30)
