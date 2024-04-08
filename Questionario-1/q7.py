# receber 3 notas 
nota_1, nota_2, nota_3 = map(float, input().split())

# receber pesos para as notas
peso_1, peso_2, peso_3 = map(int, input().split())

# calculando média ponderada
media_1 = nota_1 * peso_1
media_2 = nota_2 * peso_2
media_3 = nota_3 * peso_3

# media final
media_final = (media_1 + media_2 + media_3) / (peso_1 + peso_2 + peso_3)

print("%.6f" %media_final)