from excecoes import ErroVenda, ErroRetorno

class Inventario():
    '''
    Classe que representa o inventário
    '''
    def __init__(self):
        """
        Construtor para inicializar um objeto inventário. Cria um estoque e um caixa.
        """
        self.estoque = {'laptop': [], 'tablet': [], 'celular': []}
        self.caixa = 0

    def reposicao(self, prod, qtd_prod):
        """
        Repõe o estoque de um produto.

        Args:
            prod(object produto): objeto produto que será adicionado no estoque.
            qtd_prod(int): quatidade de produto a ser adicionado no estoque.
        """
        n = 0
        try:
            while n < qtd_prod: #define o número de vezes que o objeto será adicionado na lista
                self.estoque[prod.tipo].append(prod.__str__()) #adiciona o objeto a lista
                n += 1
        except:
            print("Não foi possivel adicionar o item no estoque")

    def venda_produto(self, prod, qtd_prod):
        """
        Vende um produto que está no estoque e adiciona o seu valor ao caixa.

        Args:
            prod(object produto): objeto produto que será vendido.
            qtd_prod(int): quatidade de produto a ser vendido.
        """
        if len(self.estoque[prod.tipo]) >= qtd_prod: #verifica se há a quantidade de produto a ser vendida
            n = 0
            while n < qtd_prod: #define o número de vezes que o objeto será retirado da lista
                index = self.estoque[prod.tipo].index(prod.__str__()) #define o index do objeto a ser tirado
                self.estoque[prod.tipo].pop(index) #retira o objeto da lista
                self.caixa += prod.valor #adiciona o valore recebido da tansação no caixa
                n += 1
        else:
            raise ErroVenda()

    def retorno_produto(self, prod, qtd_prod):
        """
        Retorna o produto ao estoque, devolvendo o dinheiro.

        Args:
            prod(object produto): objeto produto que será adicionado novamente ao estoque.
            qtd_prod(int): quatidade de produto que retornará ao estoque.
        """
        if self.caixa >= prod.valor*qtd_prod: #verifica se há dinheiro no caixa para fazer o reembolso
            n = 0
            while n < qtd_prod: #define o número de vezes que o objeto será retirado da lista
                self.caixa -= prod.valor #retira o dinheiro do caixa
                self.estoque[prod.tipo].append(prod.__str__()) #adiciona o objeto na lista
                n += 1
        else:
            raise ErroRetorno()