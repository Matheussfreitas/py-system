produtos = ['heineken','budweiser','stella','becks','corona']
print(produtos)
produto_entra = input('Qual produto deseja adicionar a lista? ')
produtos.append(produto_entra)
print('A nova lista é {}'.format(produtos))
produto_sai = input('Qual produto deseja remover da lista? ')
if produto_sai in produtos:
    produtos.remove(produto_sai)
    print('A nova lista é {}'.format(produtos))
else:
    print('Esse item não está presente na lista')