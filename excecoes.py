#Add classes de tratamento de erros nas vendas e retornos

class ErroVenda(Exception):
    def __init__(self, message="Quantidade não disponível no estoque"):
        self.message = message
        super().__init__(self.message)

class ErroRetorno(Exception):
    def __init__(self, message="Sem dinheiro para retornar ao cliente"):
        self.message = message
        super().__init__(self.message)
