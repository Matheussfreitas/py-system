qntd_hospedes = int(input('Qual a quantidade de pessoas no quarto? '))
quarto = []

if qntd_hospedes > 4:
    print('Temos quartos apenas de 1 a 4 pessoas.')
else:
    pass

for i in range(qntd_hospedes):
    nome = input('Digite o nome do hóspede: ')
    cpf = input('Digite o CPF do hóspede(apenas números): ')
    if nome and cpf:
        if len(cpf) == 11 and cpf.isnumeric():
            pass
        else:
            print('O CPF é inválido')
    else:
        print('Nome ou CPF inválido')
    hospedes = [nome, cpf]
    quarto.append(hospedes)

print(quarto)
print('Quarto reservado com sucesso!')
