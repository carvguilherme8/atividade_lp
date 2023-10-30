class Produto():

    def __init__(self, nome, valor, cod_barras):
        self.nome = nome
        self.valor = valor
        self.cod_barras = cod_barras        


class Celular(Produto):

    def __init__(self, name, valor, cod_barras, marca, tamanho, memoria_ram):
        super().__init__(self, name, valor, cod_barras)
        self.marca = marca
        self.tamanho = tamanho
        self.mamoria_ram = memoria_ram

class Laptop(Produto):
    
    def __init__(self, name, valor, cod_barras, marca, tamanho, memoria_ram, memoria_vram, freq_processador):
        super().__init__(name, valor, cod_barras)
        self.marca = marca
        self.tamanho = tamanho
        self.memoria_ram = memoria_ram
        self.memoria_vram = memoria_vram
        self.freq_processador = freq_processador

class Tablet(Produto):
    def __init__(self, name, valor, cod_barras, marca, tamanho, memoria_ram, possui_caneta):
        super().__init__(self, name, valor, cod_barras)
        self.marca = marca
        self.tamanho = tamanho
        self.memoria_ram = memoria_ram
        self.possui_caneta = possui_caneta