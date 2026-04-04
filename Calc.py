import os
import platform
from Livraria import Livro
##################################

def LimparTerminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def ListarTudo(lista_livros):
    if not lista_livros:
        print('=' * 30)
        print("A biblioteca está vazia.")
        print('=' * 30)
        return    
    for livro in lista_livros:
        print('=' * 30)
        print("\n--- Listagem de Livros ---")
        print('=' * 30)
        print(livro)


def BuscaTitulo(nome, lista_livros):
    achou = False
    for livro in lista_livros:
        if nome.lower() in livro.titulo.lower():
            print('=' * 30)
            print(f'Resultado para o título "{nome}"...')
            print('=' * 30)
            print(livro)
            achou = True
    if not achou:
        print('=' * 30)
        print('Título não disponível na biblioteca.')
        print('=' * 30)


def BuscarCategoria(categoria, lista_livros):
    achou = False
    for livro in lista_livros:
        if categoria.lower() in livro.area.lower():
            print('=' * 30)
            print(f'Resultado de livros para o categoria "{categoria}"...')
            print('=' * 30)
            print(livro)
            achou = True
    if not achou:
        print('=' * 30)
        print('Não encontrado livros para categoria inserida.')
        print('=' * 30)


def ValorLivro(valor_ref, lista_livros):
    limite = float(valor_ref)
    achou = False
    for livro in lista_livros:
        if livro.valor < limite:
            print('=' * 30)
            print(f'Livros com valores menores que R$ {limite:.2f}') 
            print('=' * 30)
            print(livro)
            achou = True
    if not achou:
        print('=' * 30)
        print('Nenhum livro menor que o valor inserido.')
        print('=' * 30)

def BuscaEstoque(estoque, lista_livros):
    estoque = int(estoque)
    achou = False
    for livro in lista_livros:
        if estoque >= livro.qtd_estoque:
            print('=' * 30, 'Listagem de livros baseada na quantidade informada...', '=' * 30)
            print(livro)
            achou = True
    if not achou:
        print('=' * 30)
        print(f'Não disponível abaixo dessa quantidade.')
        print('=' * 30)

def ValorTotalBiblioteca(lista_livros):
    total = 0.0
    for livro in lista_livros:
        total += livro.valor
    ('=' * 30)
    print(f'Valor total na biblioteca: R$ {total:.2f}')
    ('=' * 30)
    if not lista_livros:
        print(f'Biblioteca Vazia. Total de R$ {total:.2f}')

    