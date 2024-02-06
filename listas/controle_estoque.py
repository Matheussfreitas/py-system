produtos = ['heineken','budweiser','stella','becks','corona']
estoque = [16,12,8,10,6]
produto = input('Informe o nome do produto: ')
if produto in produtos:
    i = produtos.index(produto)
    qntd = estoque[i]
    print('A quantidade de {} é de {} unidades'.format(produto, qntd))
else:
    print('Não temos esse produto em estoque.')
