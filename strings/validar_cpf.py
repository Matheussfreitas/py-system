cpf = input("Digite seu CPF (apenas números): ")
cpf = cpf.strip() #tira os espaços
cpf = cpf.replace(".", "") #tira os .
cpf = cpf.replace("-", "") #tira os -

if not len(cpf) == 11 and cpf.isnumeric():
    print("Digite seu CPF corretamente.")
else:
    print(cpf)