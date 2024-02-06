meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
vendas_prim_semestre = [7490,8200,5875,7200,910,10040]
vendas_seg_semestre = [9880,11350,4000,8500,7300,5500]
vendas_anual = vendas_prim_semestre + vendas_seg_semestre

maior_venda = max(vendas_anual)
i = vendas_anual.index(maior_venda)
melhor_mes = meses[i]

menor_venda = min(vendas_anual)
j = vendas_anual.index(menor_venda)
pior_mes = meses[j]

faturamento_total = sum(vendas_anual)
percentual = maior_venda / faturamento_total

print(f'O melhor mês do ano foi {melhor_mes} com {maior_venda} vendas. \nJá o pior mês foi o de {pior_mes} com {menor_venda} vendas')
print('Portanto o faturamento anual total é de R${:,}. E a maior venda equivale a {:.1%} do faturamento total.'.format(faturamento_total, percentual))