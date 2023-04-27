class prod:
    def __init__(self,nome, codigo, preco, qtdestoque):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.qtdestoque = qtdestoque
        
        
class ListarProd:
    def __init__(self):
        self.prods = []
        
    # ADICIONAR PRODUTO PARTE 3    
    def adicionar_prod(self, produto):
        self.prods.append(produto)
        
    # REMOVER PRODUTO PARTE 3
    def remover_prod(self, produto):
        self.prods.remove(produto)
    print('-------------PARTE 1-------------')
        
    #LISTAR PRODUTOS   
    def ListarProds(self):
        for produto in self.prods:
            print(produto.__dict__)
    
    #BUSCAR PRODUTOS           
    def BuscarProd(self, nome):
        for prod in self.prods:
            if prod.nome == nome:
                return prod
        return None
lista_produto = ListarProd()

prod1 = prod('Tesla', 26, 82892, 25)
lista_produto.adicionar_prod(prod1)

prod2 = prod('Titan CG 150', 1, 11500, 10)
lista_produto.adicionar_prod(prod2)

prod3 = prod('Saveiro', 8, 50999, 5)
lista_produto.adicionar_prod(prod3)

lista_produto.ListarProds()



# FUNCAO PARA ORDENAR ELEMENTOS NA LISTA
def selection_sort(L):
    cont = 0
    for i in range(0, len(L)-1):
        menor = i
        for j in range(i+1, len(L)):
            if L[j] < L[menor]:
                menor = j
            cont+=1
        L[i], L[menor] = L[menor], L[i]
    return L


# ORDENACAO PARTE 1
print('\n----------PARTE 1 ORDENANDO OS ELEMENTOS DA LISTA----------\n')
L = [prod1.nome, prod2.nome,prod3.nome]
print(selection_sort(L))


# BUSCAR PRODUTO NA LISTA PARTE 2
print('\n----------PARTE 2 BUSCA DO PRODUTO PELA CHAVE----------\n')
encontrar_prod = lista_produto.BuscarProd('Saveiro')
if encontrar_prod:
    print('Produto encontrado: ', encontrar_prod.__dict__)
else:
    print('produto não encontrado')

prod4 = prod('Idea', 320, 2000, 200)

#PARTE 3 ADICIONANDO PRODUTO 4
print('\n----------PARTE 3 ADICIONANDO PRODUTO 4----------\n')
lista_produto.adicionar_prod(prod4)
lista_produto.ListarProds()

#PARTE 3 REMOVENDO PRODUTO 4
print('\n----------PARTE 3 REMOVENDO PRODUTO 4----------\n')
lista_produto.remover_prod(prod4)
lista_produto.ListarProds()
    