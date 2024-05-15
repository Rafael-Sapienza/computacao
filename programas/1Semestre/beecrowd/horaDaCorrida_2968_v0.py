import math

def percentual(voltas,placas):
    i = 10
    linha = ''
    while i <= 90:
        total = voltas*placas
        percentual = i*total/100
        percentual = math.ceil(percentual)
        if i == 90:
            linha += f'{percentual}' 
        else:
            linha += f'{percentual}' + ' '
        i += 10
    print(linha)

voltas,placas = [int(r) for r in input().split()]        
percentual(voltas,placas)        