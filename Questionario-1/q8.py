"""
Recebe a, b e c
Multiplica p1 por a + b
Multiplica p2 por c + d
Concatena o resultado
Multiplica o ultimo passo por a + c e concatena no final
"""

a = int(input())
b = int(input())
c = int(input())

char_1 = input()
char_2 = input()

parte_1 = (a + b) * char_1
parte_2 = (b + c) * char_2
junta_p1_p2 = parte_1 + parte_2

ultimo_resultado = (a + c) * junta_p1_p2

print(ultimo_resultado)