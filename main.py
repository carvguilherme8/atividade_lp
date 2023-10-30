import produtos as prod
import inventario as inv

# Criando inventário
inventario = inv.Inventario()


# Criando objetos produtos
nitro_5 = prod.Laptop("Nitro 5", 4199, "1111111", prod.Marcas(2).name, "15,6", "8GB", "4GB", "4,5 GHz") #cria um objeto laptop
tab_s6 = prod.Tablet("Galaxy Tab S6 Lite", 1729, "2222222", prod.Marcas(1).name, "10,4", "4GB", True) #cria um objeto tablet
smartphone_xiaomi_x5 = prod.Celular("Xiaomi X5", 1853, "3333333", prod.Marcas(6).name, "9,0", "6GB") #cria um objeto smartphone
tab_s9 = prod.Tablet("Samsung Galaxy Tab S9", 5399, "4444444", prod.Marcas(1).name, "11,0", "8GB", True) #cria um objeto tablet

# Movimentando produtos no estoque com os métodos criados

                                         # Utilizando os métodos criado para:
inventario.reposicao(nitro_5, 5)         # Repor 5 Nitro 5 no estoque
inventario.venda_produto(nitro_5, 3)     # Vender 3 Nitro 5 
inventario.retorno_produto(nitro_5, 1)   # Devolver 1 Nitro 5 ao estoque

inventario.reposicao(tab_s6, 3)
inventario.venda_produto(tab_s6, 1) 
inventario.retorno_produto(tab_s6, 1)

inventario.reposicao(smartphone_xiaomi_x5, 6)
inventario.venda_produto(smartphone_xiaomi_x5, 4) 
inventario.retorno_produto(smartphone_xiaomi_x5, 2)

inventario.reposicao(tab_s9, 6)
inventario.venda_produto(tab_s9, 3) 
inventario.reposicao(tab_s9, 1)

#Para dar erro
# inventario.venda_produto(tab_s9, 8) 
# inventario.retorno_produto(tab_s9, 20)

print(f"Dinheiro no caixa: {inventario.caixa}")  
print(f"Estoque: {inventario.estoque}")
