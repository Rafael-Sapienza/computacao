def makeMatrix(L,C):
    matriz = []
    for _ in range(L):
        linha = [int(r) for r in input().split()]
        matriz.append(linha)
    return matriz

def ehUmaMatrizLegal(matriz):
    flag = True
    numeroDeLinhas = len(matriz)
    numeroDeColunas = len(matriz[0])
    primeiro = matriz[0][0]
    for i in range(1,numeroDeLinhas):
        for j in range(1,numeroDeColunas):
            if primeiro + matriz[i][j] > matriz[0][j] + matriz[i][0]:
                flag = False
                break
    return flag

def ehUmaMatrizSuperLegal(matriz):
    numeroDeLinhasDaMatriz = len(matriz)
    numeroDeColunasDaMatriz = len(matriz[0])
    flag = True
    for numeroDeLinhasDaSubmatriz in range(2,len(numeroDeLinhasDaMatriz)+1):
        if flag:
            for numeroDeColunasDaSubmatriz in range(2,len(numeroDeColunasDaMatriz)+1):
                submatriz = [[0]*numeroDeColunasDaSubmatriz]*numeroDeLinhasDaMatriz
                if flag:
                    for i in range(numeroDeLinhasDaMatriz - numeroDeLinhasDaSubmatriz):
                        if flag:
                            for j in range(numeroDeColunasDaMatriz - numeroDeColunasDaSubmatriz):
                                if flag:
                                    for i1 in range(i,i+numeroDeLinhasDaSubmatriz):
                                        for j1 in range(j,j+numeroDeColunasDaSubmatriz):
                                            submatriz[i1-i][j1-j] = matriz[i1][j1]
                                    if not(ehUmaMatrizLegal(submatriz)):
                                        flag = False
                                        break
    return flag
                    

