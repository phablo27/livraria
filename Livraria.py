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

# def Exibir(self):
#     for info in self.historico:
#         print(info)



        
        