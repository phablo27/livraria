from Calc import LimparTerminal, ListarTudo, BuscaTitulo, BuscarCategoria, ValorLivro, ValorTotalBiblioteca, BuscaEstoque
from Livraria import Livro
biblioteca = []   

def menu():
    print('=' * 30)
    print('Sistema liberado...')
    print('=' * 30)
########################################
    print('1 - Cadastrar novo livro')
    print('2 - Listar livros')
    print('3 - Buscar livros por nome')
    print('4 - Buscar livros por categoria')
    print('5 - Buscar livros por preço')
    print('6 - Buscar por quantidade em estoque')
    print('7 - Valor total no estoque')
    print('0 - Encerrar atividades')

while True:
    LimparTerminal()
    menu()
    print()
  
    opcao = input('Selecione a opção: ')
    print('=========================')
    LimparTerminal()

    match opcao:
        case '1':
            print('=' * 15, 'CADASTRANDO LIVRO...', '=' * 15,)
            print()

            titulo = input('Nome do livro: ')
            cod = input('Código do livro: ')
            editora = input('Nome da editora: ')
            area = input('Genêro do livro: ')
            ano = int(input('Ano do livro: '))
            valor = float(input('Valor do livro: '))
            qtd_estoque = int(input('Quantidade em estoque do livro: '))  
            
            #Incluíndo livro
            novo_livro = Livro(titulo, cod, editora, area, ano,  valor, qtd_estoque)
            biblioteca.append(novo_livro)
            print()
            print('=============================')
            print('Livro cadastrado com sucesso!')
            print('=============================')
            input("\nPressione [Enter] para voltar ao menu...")

            LimparTerminal()
        
        case '2':
            ListarTudo(biblioteca)
            input("\nPressione [Enter] para voltar ao menu...")

            LimparTerminal()

        case '3':
            try:
                busca_nome = input('Digite um nome de livro: ')
                BuscaTitulo(busca_nome, biblioteca)
                input("\nPressione [Enter] para voltar ao menu...")

                LimparTerminal()

            except ValueError:
                print('Erro: Digite apenas letras/palavras')
                input("\nPressione [Enter] para voltar ao menu...")

        case '4':
            try:
                busca_categoria = input('Digite um genêro de livro: ')
                BuscarCategoria(busca_categoria, biblioteca)
                input("\nPressione [Enter] para voltar ao menu...")
                LimparTerminal()

            except ValueError: 
                print('Erro: Digite apenas letras/palabras')
                input("\nPressione [Enter] para voltar ao menu...")

        case '5':
            try:
                busca_valor = float(input('Selecione um preço de referência: '))
                ValorLivro(busca_valor, biblioteca)
                input("\nPressione [Enter] para voltar ao menu...")
                LimparTerminal()

            except ValueError:
                print("Erro: Digite apenas números para o preço.")
                input("\nPressione [Enter] para voltar ao menu...")

        case '6':
            busca_estoque = int(input('Digite quantidade de estoque para verificação na biblioteca: '))
            BuscaEstoque(busca_estoque, biblioteca)
            input("\nPressione [Enter] para voltar ao menu...")
            LimparTerminal()

        case '7':
            ValorTotalBiblioteca(biblioteca)       
            input("\nPressione [Enter] para voltar ao menu...")
            LimparTerminal()

        case '0':
            print('Encerrando...')
            break
