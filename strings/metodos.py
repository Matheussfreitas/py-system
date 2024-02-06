texto = 'matheus freitas' 
mail = 'mgsoutodelira@gmail.com'
intro = '''Oi, sou matheus
tudo bem com vc?
tchau'''
print(texto.capitalize()) #1° letra maiuscula
print(texto.casefold()) #todas as letras minusculas
print(texto.count('e')) #quantidade de vezes que um valor aparece na string
print(texto.endswith('tas')) #verifica se a string termina com o valor em especifico com true ou false
print(texto.find('h')) #procura um texto dentro de outro e retorna a posição do valor em especifico
print(texto.isalnum()) #verifica se tem letras e números
print(texto.isalpha()) #verifica se tem apenas letras
print(texto.isnumeric()) #verifica se tem apenas números
print(texto.replace('m','f')) #troca um valor por outro
print(mail.split('@')) #separa uma string com base em um delimitador 
print(intro.splitlines()) #separa a string com base nos 'enters'
print(texto.startswith('mat')) #verifica se começa com um valor em especifico
print(texto.strip(' ')) #retira caracteres indesejados do texto, usando mais em ' '
print(texto.upper()) #todas as letras maiusculas
print(texto.title()) #coloca a 1° letra de cada palavra em maiuscula