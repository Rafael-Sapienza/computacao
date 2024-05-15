'''def quantasEscadinhas(tamanho,lista):
    counter = 0
    razaoAntiga = lista[1] - lista[0]
    i = 0
    while i <= tamanho - 2 and tamanho >= 2:
        item0 = lista[i]
        item1 = lista[i+1]
        if item1 - item0 != razaoAntiga:
            lista = lista[i+1:]
            tamanho -= (i+1)
            counter += 1
            if tamanho >= 2:
              razaoAntiga = lista[1] - lista[0]
            i = 0
        i += 1
    counter += 1
    print(counter)'''




lissta = [2,2,1,3,4,4]
lissta =set(lissta)
lissta = list(lissta)
print(lissta)














tamanho = int(input())
lista = [int(t) for t in input().split()]


