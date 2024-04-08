word_1, word_2, word_3 = input().split()

# concatenando word_1, word_2 e word_3
"""
Para formar uma nova onomatopeia eles juntam a primeira string com três ocorrências da segunda e duas da terceira
"""
onomatopeia = word_1 + (word_2 * 3) +(word_3 * 2)
print(onomatopeia)