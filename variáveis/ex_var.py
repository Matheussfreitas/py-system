qnte_coca = 200
qnte_pepsi = 150
preco_coca = 2.50
preco_pepsi = 2.00
custo_loja = 2000

faturamento_coca = qnte_coca * preco_coca
faturamento_pepsi = qnte_pepsi * preco_pepsi
faturamento_total = faturamento_coca + faturamento_pepsi

lucro = faturamento_total - custo_loja
margem = lucro / faturamento_total

print("O faturamento com Coca Cola é de {} o faturamento da Pepsi é de {} e o faturamento total é {}".format(faturamento_coca, faturamento_pepsi, faturamento_total))
print("O lucro da loja é de {} e a margem é {}".format(lucro, margem))