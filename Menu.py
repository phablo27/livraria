from Livraria import Livro
biblioteca = []   

def menu():
    print('=' * 30)
    print('Sistema liberado...')
    print('1 - Cadastrar novo livro')
    print('2 - Listar livros')
    print('3 - Buscar livros por nome')
    print('4 - Buscar livros por categoria')
    print('5 - Buscar livros por preço')
    print('6 - Buscar por quantidade em estoque')
    print('0 - Encerrar atividades')

while True:
    menu()
    print()

    opcao = input('Selecione a opção: ')
    print('=========================')

    match opcao:
        case '1':
            titulo = input('Nome do livro: ')
            cod = input('Código do livro: ')
            editora = input('Nome da editora: ')
            area = input('Genêro do livro: ')
            valor = float(input('Valor do livro: '))
            qtd_estoque = int(input('Quantidade em estoque do livro: '))  
            
            #Incluíndo livro
            novo_livro = Livro(titulo, cod, editora, area, valor, qtd_estoque)
            biblioteca.append(novo_livro)
            print('Livro cadastrado com sucesso')
        
        case '2':
            if novo_livro in biblioteca:
                for info in biblioteca:
                    print(info)

        case '3':
            nome = input('Digite um nome de livro: ')
            if nome in biblioteca:
                print(biblioteca)
                for n in nome:
                    print(f'{nome} disponível na biblioteca.')
            else:
                print('Livro indisponível. Necessita cadastro na biblioteca!')
        case '4':
            print()
        case '5':
            print()
        case '6':
            print()
        case '0':
            print('Encerrando...')
            break
