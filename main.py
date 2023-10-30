import produtos as prod
import inventario as inv

inventario = inv.Inventario()

nitro_5 = prod.Laptop("Nitro 5", 4199, "1111111", prod.Marcas(2).name, "15,6”", "8GB", "4GB", "4,5 GHz")



inventario.reposicao(nitro_5, 5)

inventario.venda_produto(nitro_5, 3)

inventario.retorno_produto(nitro_5, 1)

print(inventario.caixa)
print(inventario.estoque)