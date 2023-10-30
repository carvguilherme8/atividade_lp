from enum import Enum

class Marcas(Enum):
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
    Classe base para os produtos
    '''
    def __init__(self, nome, valor, cod_barras, marca, tipo):
        self.nome = nome
        self.valor = valor
        self.cod_barras = cod_barras
        self.tipo = tipo
        self.marca = marca        

class Celular(Produto):
    '''
    Essa classe representa um celular, ela é herdada da classe produto
    '''
    def __init__(self, name, valor, cod_barras, marca, tamanho, memoria_ram):
        super().__init__(self, name, valor, cod_barras, marca, tipo = "celular")
        self.tamanho = tamanho
        self.mamoria_ram = memoria_ram

class Laptop(Produto):
    '''
    Essa classe representa um laptop, ela é herdada da classe produto
    '''
    def __init__(self, name, valor, cod_barras, marca, tamanho, memoria_ram, memoria_vram, freq_processador):
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
        super().__init__(self, name, valor, cod_barras, marca, tipo = "tablet")
        self.tamanho = tamanho
        self.memoria_ram = memoria_ram
        self.possui_caneta = possui_caneta