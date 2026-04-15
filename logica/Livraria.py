# from Calc import valorLivro
class Livro():
    def __init__(self, titulo, cod, editora, area, ano, valor, carrega_arquivo, atualiza_arquivo, qtd_estoque):
        self.titulo = titulo
        self.cod = cod 
        self.editora = editora 
        self.area = area 
        self.ano = ano
        self.valor = valor
        self.carrega_livro = carrega_arquivo
        self.atualiza_arquivo = atualiza_arquivo
        self.qtd_estoque = qtd_estoque

        self.total = (qtd_estoque * valor)

    def __str__(self):
        return(f'>>>>>>>cod#{self.cod}\n'
               f'Título/Editora: {self.titulo}/{self.editora}\n'
               f'Categoria: {self.area}\n'
               f'Ano: {self.ano}\n'
               f'Valor: R$ {self.valor:.2f}\n'
               f'Estoque: {self.qtd_estoque}\n'
               f'Valor total em estoque: R$ {self.total:.2f}\n')                     
        