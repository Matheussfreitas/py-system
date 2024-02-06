produtos = ['apple','samsung','xiaomi','motorola','nokia','LG']
vendas_2023 = [74246,87234,82973,98387,74937,83928]
vendas_2024 = [81724,74832,98974,84729,84782,81832]

for i, produto in enumerate(produtos):
    if vendas_2024[i] > vendas_2023[i]:
        percentual = vendas_2024[i] / vendas_2023[i] - 1
        print('{}: 2023 - {:,} / 2024 - {:,} / {:.1%} de aumento'.format(produto, vendas_2023[i], vendas_2024[i], percentual))