def makeMatrix(G):
    matriz = []
    for _ in range(G):
        L = [int(r) for r in input().split()]
        matriz.append(L)
    return matriz


sistemaDePont = [5, 3, 2]
k = len(sistemaDePont)



def qualAPontDeCadaPiloto(P,k,matriz,sistemaDePont):
    pontDeCadaPiloto = [0]*(P)
    for item in matriz:
        for i in range(k):
            piloto = item[i]
            pontDeCadaPiloto[piloto-1] += sistemaDePont[i]
    return pontDeCadaPiloto


def quaisOsPilotosVencedores(pontDeCadaPiloto):
    myDict = {}
    '''for i,item in enumerate(pontDeCadaPiloto,start=1):
        piloto = i
        pontDoPiloto = item
        myDict[piloto] = pontDoPiloto
    inv = {}
    for key,value in myDict:
        if value not in inv:
            inv[value] = key
        else:
            inv[value].append(key)'''
    for i,item in enumerate(pontDeCadaPiloto,start=1):
        piloto = i
        pontDoPiloto = item
        if pontDoPiloto not in myDict:
            myDict[pontDoPiloto] = [piloto]
        else:
            myDict[pontDoPiloto].append(piloto)
    L = sorted(myDict,reverse=True)
    pilotosVencedores  = myDict[L[0]]
    pilotosVencedores.sort()
    print(*pilotosVencedores)


def main():
    G,P = [int(r) for r in input().split()]
    while G!=0 or P!=0:
        matriz = makeMatrix(G)
        S = int(input())
        for _ in range(S):
            L = [int(j) for j in input().split()]
            k = L[0]
            sistemaDePont = L[1:]
            pontDeCadaPiloto = qualAPontDeCadaPiloto(P,k,matriz,sistemaDePont)
            quaisOsPilotosVencedores(pontDeCadaPiloto)
        G,P = [int(r) for r in input().split()]

main()








