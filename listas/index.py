produtos = ['pc','xbox','ps4','xone','ps5']
estoque = [5,7,10,4,12]

i = produtos.index('xone') #retorna o indice do item na lista
qntd = estoque[i]
print('A quantidade em estoque do produto é de: {}'.format(qntd))