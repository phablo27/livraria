from Livraria import Livro

biblioteca = []   

def menu():
    print('1 - Cadastrar novo livro')
    print('2 - Listar livros')
    # print('3 - Buscar livros por nome')
    # print('4 - Buscar livros por categoria')
    # print('5 - Buscar livros por preço')
    # print('6 - Buscar por quantidade em estoque')
    print('0 - Encerrar atividades')

while True:
    menu()
    opcao = input('Selecione a opção: ')

    match opcao:
        case '1':
            titulo = input('Nome do livro: ')
            cod = input('Código do livro: ')
            editora = input('Nome da editora: ')
            area = input('Qual genêro do livro: ')
            valor = float(input('Valor do livro: '))
            qtd_estoque = int(input('Quantidade em estoque do livro: '))  

            novo_livro = Livro(titulo, cod, editora, area, valor, qtd_estoque)
            biblioteca.append(novo_livro)
            print('Livro cadastrado com sucesso')
            print(biblioteca)
        
        case '2':
            if novo_livro in biblioteca:
                for info in biblioteca:
                    print(info )
        
        case '0':
            print('Encerrando...')
            break
