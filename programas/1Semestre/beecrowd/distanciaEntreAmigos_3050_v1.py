def nextTerm(i,N,alturasDosPredios):
# nao vale a pena iterar de i=1 ate i =N-1. No lugar, se vc passar novamente por um predio de 
#tamanho menor ou igual a um anterior, 
#despreze-o, pois a distancia percorrida no bloco terreo diminui a medida que i aumenta
    flag = False
    for r in range(i+1,N):
        if alturasDosPredios[r]>alturasDosPredios[i]:
            i = r
            flag = True
            return i
            break
    if not(flag):
        return -1


def qualAMaiorDistancia(N, i = 0):
    alturasDosPredios = [int(r) for r in input().split()]
    flag = False
    maiorDistancia = alturasDosPredios[0] +1 + alturasDosPredios[1]
    while True:
        if flag:
            i = nextTerm(i,N,alturasDosPredios)         
        flag = True
        if i == -1:
            print(maiorDistancia)
            break
        for j in range(i+1,N):
            distancia = alturasDosPredios[i] + j - i + alturasDosPredios[j]              
            if distancia>maiorDistancia:
                maiorDistancia = distancia

N = int(input())
qualAMaiorDistancia(N)