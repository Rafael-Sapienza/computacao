def qualSeraAProximaFileira(comp,fileira):
    proxFileira = (comp-1)*[0]
    for i in range(len(proxFileira)):
        if fileira[i] == fileira[i+1]:
            proxFileira[i] = 1
        else:
            proxFileira[i] = -1
    return proxFileira

def qualSeraAUltimaBola(n,primeiraFileira):
    proxFileira = primeiraFileira
    comp = n
    while comp >= 2:
        proxFileira = qualSeraAProximaFileira(comp,proxFileira)
        comp -=1
    if proxFileira == [1]:
        print('preta')
    else:
        print('branca')

n = int(input())
primeiraFileira = [int(r) for r in input().split()]
qualSeraAUltimaBola(n,primeiraFileira)