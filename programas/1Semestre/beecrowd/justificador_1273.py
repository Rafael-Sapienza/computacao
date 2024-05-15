def justifique(L):
    listaDeComprimentos = []
    for item in L:
        listaDeComprimentos.append(len(item))
    maiorComprimento = max(listaDeComprimentos)
    for item in L:
        gaps = (maiorComprimento - len(item))*' '
        stringJustificada = gaps + item
        print(stringJustificada)



def main():
    n = int(input())
    L = []
    for _ in range(n):
        s = input()
        L.append(s)
    justifique(L)
    n = int(input())
    while n != 0:
        print()
        L = []
        for _ in range(n):
            s = input()
            L.append(s)
        justifique(L)
        n = int(input())



main()