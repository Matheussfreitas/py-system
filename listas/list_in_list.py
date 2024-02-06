vendedores = ['matheus','mariana','luiz','hebert']
produtos = ['iphone','ipad']
vendas = [[200,100],
          [100,100],
          [150,50],
          [50,50]
]

#adicionando um novo produto a lista de produtos
imac = [50,30,20,15]
produtos.append('imac')
vendas[0].append(imac[0])
vendas[1].append(imac[1])
vendas[2].append(imac[2])
vendas[3].append(imac[3])
print(vendas)

#alterando um valor dentro das listas
novo_valor = [50,20,40,30]
vendas[0][0] = novo_valor[0]
vendas[1][0] = novo_valor[1]
vendas[2][0] = novo_valor[2]
vendas[3][0] = novo_valor[3]
print(vendas)
