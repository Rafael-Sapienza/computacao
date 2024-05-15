def makeVector(T):
    L = []
    for i in range(1000):
        valor = i % T
        L.append(valor)
    for index,item in enumerate(L):
        print(f'N[{index}] = {item}')

T = int(input())
makeVector(T)   
