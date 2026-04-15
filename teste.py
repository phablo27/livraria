def CarregaArquivos ():
    with open("livros_cliente.txt", 'r', encoding='uft-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip().split(',')
            print(linha)

CarregaArquivos()