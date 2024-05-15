def makeVector(n):
    L = []
    termo = n
    L.append(termo)
    for i in range(9):
        termo *= 2
        L.append(termo)
    for i in range(10):
        print(f'N[{i}] = {L[i]}')



n = int(input())
makeVector(n)