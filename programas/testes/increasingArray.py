def quantosMovimentosNoMinimo(lista):
    item0 = lista[0]
    counter = 0
    for i,item in enumerate(lista):
        if item<item0:
            counter += item0-item
            lista[i] = item0
        else:
            item0 = item
    return counter

n = input()
lista = [int(r) for r in input().split()]
numeroMinimoDeMovimentos = quantosMovimentosNoMinimo(lista)
print(numeroMinimoDeMovimentos)