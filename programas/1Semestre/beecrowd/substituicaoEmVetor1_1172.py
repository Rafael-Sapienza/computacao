def substituaOVetor():
    L = []
    for _ in range(10):
        x = int(input())
        L.append(x)
    for i in range(10):
        if L[i] <= 0:
            L[i] = 1
    for i in range(10):
        x = L[i]
        print(f'X[{i}] = {x}')


substituaOVetor()