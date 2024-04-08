# receber sabor e pedaços 
sabor, pedacos = input().split()

# calcular preço da fatia
preco_fatia = 3.25 * int(pedacos)

# formar frase 
print("Foram %s pedaços de bolo de %s, então fica R$ %.2f reais" %(pedacos, sabor, preco_fatia))
