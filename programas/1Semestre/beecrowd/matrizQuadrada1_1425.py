def makeMatrix(n):
    if n%2 == 1:
        if n == 1:
            print(1)
        else:
            counter = 1
            L = []
            primeiraLinha = [1]*n
            printNovo(primeiraLinha)
            while counter<=n//2:
                L.append(counter)
                linha = L + [counter+1]*(n-2*counter) + L[::-1]
                counter += 1
                printNovo(linha)
            counter = n//2 - 1
            while counter>=1:
                L.pop()
                linha = L + [counter+1]*(n-2*counter) + L[::-1]
                counter -= 1
                printNovo(linha)
            printNovo(primeiraLinha)
    if n%2 == 0:
        counter = 1
        L = []
        primeiraLinha = [1]*n
        printNovo(primeiraLinha)
        while counter<=n//2 -1:
            L.append(counter)
            linha = L + [counter+1]*(n-2*counter) + L[::-1]
            counter += 1
            printNovo(linha)
        counter = n//2 - 1
        while counter>=1:
            linha = L + [counter+1]*(n-2*counter) + L[::-1]
            counter -= 1
            printNovo(linha)
            L.pop()
        printNovo(primeiraLinha)



def printNovo(linha):
    s = ''
    s += '  ' + f'{linha[0]}'
    for item in linha[1:]:
        if item >= 1 and item <=9:
            subtring = '   ' + f'{item}' 
        if item >= 10 and item <= 99:
            subtring = '  ' + f'{item}'
        if item >= 100:
            substring = ' ' + f'{item}'
        s += subtring
    print(s)




def solveProblem():
    n = int(input())
    while n != 0:
        makeMatrix(n)
        print()
        n = int(input())
        


solveProblem()
