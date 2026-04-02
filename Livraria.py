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
        return f'{self.historico}'

    def Exibir(self):
        self.historico.split()
        print(self.Historico)

objeto = Livro('Sapiens', '1133','Dark Side','Científico','100','29') 

objeto.Historico()
    # def historicoValor(self):
    #     valores = []
    #     valores.append(self.list)

    # #Exibição do menu
    # def Menu(self, opcap):
    #     match opcap:
    #         case 1:
    #             return
    #         case 2:
    #             return
    #         case 3:
    #             return
        
    # #Pesquisa do livro

    # def Valor(self):
    #     valorLivro()
        
        