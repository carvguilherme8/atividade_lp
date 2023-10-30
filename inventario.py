class ErroVenda(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Inventario:
    def __init__(self):
        self.estoque = {}

    def reposicao(self, prod, qtd_prod):
        if prod in self.estoque:
            self.estoque[prod] += qtd_prod
        else:
            self.estoque[prod] = qtd_prod

    def venda_prod(self, prod, qtd_prod):
        if prod in self.estoque and self.estoque[prod] >= qtd_prod:
            self.estoque[prod] -= qtd_prod
        else:
            raise ErroVenda("Quantidade não disponível no estoque")

    def retorno_prod(self, prod, qtd_prod):
        if prod in self.estoque:
            self.estoque[prod] += qtd_prod
        else:
            self.estoque[prod] = qtd_prod

# Cria uma instância da classe Inventario
inventario = Inventario()

inventario.venda_prod("camisa",2)
inventario.venda_prod("camisa",3)

print(inventario.estoque)

