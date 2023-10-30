from enum import Enum

class Marcas(Enum):
    """
    Classe que cria as enumerações das marcas.
    """
    Samsung = 1
    Acer = 2
    Lenovo = 3
    Apple = 4
    Motorola = 5
    Xaomi = 6
    Positivo = 8
    Dell = 7
    Asus = 10
    Google = 9

class Produto():
    '''
    Classe base para os produtos.
    '''
    def __init__(self, nome, valor, cod_barras, marca, tipo):
        """
        Construtor para inicializar um objeto produto genérico.

        Args:
            nome(str): Nome do produto.
            valor(float): preço do produto.
            cod_barras(int): codigo de barras do produto.
            marca(str): marca do produto
            tipo(str): tipo do produto (Ex: "celular")
        """
        self.nome = nome
        self.valor = valor
        self.cod_barras = cod_barras
        self.tipo = tipo
        self.marca = marca

    def __str__(self):
        """String que representa o produto.

        Retorna:
            str: Um string com o nome do produto e seu código de barras.
        """
        return f"{self.nome} {self.cod_barras}"        

class Celular(Produto):
    '''
    Essa classe representa um celular, ela é herdada da classe produto.
    '''
    def __init__(self, name, valor, cod_barras, marca, tamanho, memoria_ram):
        """
        Construtor para inicializar um objeto celular.

        Args:
            nome(str): Nome do celular.
            valor(float): preço do celular.
            cod_barras(int): codigo de barras do celular.
            marca(str): marca do celular.
            tamanho(float): tamanho da tela do celular.
            memoria_ram(str): quantidade de memoria RAM do celular (Ex: 8GB)
        """
        super().__init__(name, valor, cod_barras, marca, tipo = "celular")
        self.tamanho = tamanho
        self.mamoria_ram = memoria_ram

class Laptop(Produto):
    '''
    Essa classe representa um laptop, ela é herdada da classe produto
    '''
    def __init__(self, name, valor, cod_barras, marca, tamanho, memoria_ram, memoria_vram, freq_processador):
        """
        Construtor para inicializar um objeto Leptop.

        Args:
            nome(str): Nome do Leptop.
            valor(float): preço do Leptop.
            cod_barras(int): codigo de barras do Leptop.
            marca(str): marca do Leptop.
            tamanho(float): tamanho da tela do Leptop.
            memoria_ram(str): quantidade de memoria RAM do Leptop (Ex: 8GB)
            memoria_vram(str): quantidade de memoria de video(VRAM) do Leptop
            freq_processador(str): frequência do processador do Leptop (Ex: 3,5 GHz)
        """
        super().__init__(name, valor, cod_barras, marca, tipo = "laptop")
        self.tamanho = tamanho
        self.memoria_ram = memoria_ram
        self.memoria_vram = memoria_vram
        self.freq_processador = freq_processador

class Tablet(Produto):
    '''
    Essa classe representa um tablet, ela é herdada da classe produto
    '''
    def __init__(self, name, valor, cod_barras, marca, tamanho, memoria_ram, possui_caneta):
        """
        Construtor para inicializar um objeto Tablet.

        Args:
            nome(str): Nome do Tablet.
            valor(float): preço do Tablet.
            cod_barras(int): codigo de barras do Tablet.
            marca(str): marca do Tablet.
            tamanho(float): tamanho da tela do Tablet.
            memoria_ram(str): quantidade de memoria RAM do Tablet (Ex: 8GB)
            possuit_caneta(bool): True se o tablet vem com caneta e False se não.
        """
        super().__init__(name, valor, cod_barras, marca, tipo = "tablet")
        self.tamanho = tamanho
        self.memoria_ram = memoria_ram
        self.possui_caneta = possui_caneta