jogos = ['gta 5', 'uncharted 4', 'fifa', 'god of war', 'the last of us']
vendas = [100000, 50000, 85000, 80000, 80000]
tamanho = len(jogos)
print('Temos uma lista com os {} jogos mais vendidos do mercado'.format(tamanho))

mais_vendido = max(vendas)
i = vendas.index(mais_vendido)
jogo_mais_vendido = jogos[i]

menos_vendido = min(vendas)
j = vendas.index(menos_vendido)
jogo_menos_vendido = jogos[j]

print(f'O jogo mais vendido é o {jogo_mais_vendido} com {mais_vendido} cópias vendidas.')
print(f'E o jogo menos vendido foi o {jogo_menos_vendido} com {menos_vendido} de cópias vendidas.')

