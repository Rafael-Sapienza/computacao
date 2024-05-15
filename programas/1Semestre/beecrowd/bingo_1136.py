'''def ehPossivel(n,m,lista):
    L = []
    for i in range(m):
        for j in range(i+1,m):
            dif = abs(lista[j] - lista[i])
            L.append(dif)
    L.sort()
    L2 = []
    for i in range(len(L)-1):
        item0 = L[i]
        item1 = L[i+1]
        if item1 != item0:
            L2.append(item0)
    L2.append(L[-1])
    if len(L2) == n:
        print('Y')
    else:
        print('N')'''





def ehPossivel(n,m,lista):
    lista.sort()
    if lista[0] != 0 or lista[-1] != n:
        return 'N'
    difMax = lista[1] - lista[0]
    for i in range(len(lista) - 1):
        difNovo = lista[i+1] - lista[i]
        if difNovo > difMax:
            difMax = difNovo

    razao = difMax - 1













def main():
    n,m = [int(r) for r in input().split()]
    while n != 0 and m != 0:
        lista = [int(r) for r in input().split()]
        ehPossivel(n,m,lista)
        n,m = [int(r) for r in input().split()]

main()