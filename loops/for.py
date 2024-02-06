produtos = ['coca','pepsi','guaraná','fanta','soda']
producao = [200,150,150,100,50]
tamanho = len(produtos)

for i in range(tamanho):
    print('Foram feitas {} unidades de {}'.format(producao[i],produtos[i]))