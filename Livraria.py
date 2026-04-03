# from Calc import valorLivro
class Livro():
    def __init__(self, titulo, cod, editora, area, valor, qtd_estoque):
        self.titulo = titulo
        self.cod = cod 
        self.editora = editora 
        self.area = area 
        self.valor = valor
        self.qtd_estoque = qtd_estoque
        self.historico = [titulo, cod, editora, area, valor, qtd_estoque]
    
    def ListaLivros(self):
        for livro in self.historico:
            print(livro)

    def __str__(self):
        return(f'>>>>>>>cod#{self.cod}\n'
               f'Título/Editora: {self.titulo}/{self.editora}\n'
               f'Categoria: {self.area}\n'
               f'Valor: R$ {self.valor:.2f}\n'
               f'Estoque: {self.qtd_estoque}\n')


        
        