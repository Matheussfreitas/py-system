nome = input('Digite seu nome: ')
email = input('Digite seu email: ')

if nome and email:
    pos_a = email.find('@') #posição do @ no texto
    servidor = email[pos_a:] #posição do @ para frente
    if pos_a != -1 and '.' in servidor: #verificação da posição e do .
        print('Cadastro concluído')
    else:
        print('Nome e/ou email inválido')
else:
    print('Nome e/ou email inválido')