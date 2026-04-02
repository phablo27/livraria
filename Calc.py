from Livraria import historicoValor

def valorLivro():
    valorRef = input()
     
    for precoLivro in historicoValor:
        if  precoLivro < valorRef:
            print(historicoValor)


