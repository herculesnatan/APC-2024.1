hora, minuto, segundo = map(int, input().split(":"))
calculo_hora = hora * 3600
calculo_min = minuto * 60
calculo_final = calculo_hora + calculo_min + segundo
saida = "La se foram %i segundos que nao voltam mais..." %(calculo_final)

print(saida)