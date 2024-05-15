def makeVectors():
    par =[]
    impar = []
    counterPar = 0
    counterImpar = 0
    for i in range(15):
        x = int(input())
        if x % 2 == 0:
            par.append(x)
            counterPar += 1
        else:
            impar.append(x)
            counterImpar += 1
        if counterPar == 5:
            for i in range(5):
                item = par[i]
                print(f'par[{i}] = {item}')
            counterPar = 0
            par = []
        if counterImpar == 5:
            for i in range(5):
                item = impar[i]
                print(f'impar[{i}] = {item}')
            counterImpar = 0
            impar = []
    for i, item in enumerate(impar):
        print(f'impar[{i}] = {item}')
    for i,item in enumerate(par):
        print(f'par[{i}] = {item}')


makeVectors()