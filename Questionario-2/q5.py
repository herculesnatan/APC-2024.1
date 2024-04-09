dia, mes, ano = input().split("/")

# data no formato "DD-MM-AA";
print("%s-%s-%s" %(dia, mes, ano))
# data no formato "MM-DD-AA"; 
print("%s-%s-%s" %(mes, dia, ano))
# data no formato "AA/MM/DD".
print("%s/%s/%s" %(ano, mes, dia))