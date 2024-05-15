def qualAMaiorDistancia(N):
    alturasDosPredios = [int(r) for r in input().split()]
    for i in range(N-1):
        for j in range(i+1,N):
            distancia = alturasDosPredios[i] + j - i + alturasDosPredios[j]
            if i == 0 and j ==1:
                maiorDistancia = distancia
            if distancia>maiorDistancia:
                maiorDistancia = distancia
    print(maiorDistancia)

N = int(input())
qualAMaiorDistancia(N)