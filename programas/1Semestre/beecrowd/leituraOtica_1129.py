def qualEhALetra(lista):
    counterP = 0
    for i,item in enumerate(lista):
        if item > 127:
            lista[i] = 'B'
        else:
            lista[i] = 'P'
            counterP += 1
            if counterP == 1:
                if i == 0:
                    letra = 'A'
                elif i  == 1:
                    letra = 'B'
                elif i  == 2:
                    letra = 'C'
                elif i  == 3:
                    letra = 'D'
                elif i  == 4:
                    letra = 'E'
    if counterP != 1:
        print('*')
    else:
        print(letra)






def main():
    n = int(input())
    while n != 0:
        for _ in range(n):
            lista = [int(r) for r in input().split()]
            qualEhALetra(lista)
        n = int(input())

main()