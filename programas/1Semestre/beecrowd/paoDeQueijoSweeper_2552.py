def desenheMatrizPaoDeQueijo(n,m):
    matrizPaoDeQueijo = []
    matrizPaoDeQueijo.append([0]*(m+2))
    for i in range(n):
        L = [int(r) for r in input().split()]
        matrizPaoDeQueijo.append([0]+L+[0])
    matrizPaoDeQueijo.append([0]*(m+2))
    return matrizPaoDeQueijo



def desenheCelula(matrizPaoDeQueijo):
    celula = []
    for i in range(1,len(matrizPaoDeQueijo)-1):
        linha = []
        for j in range(1,len(matrizPaoDeQueijo[i])-1):
            if matrizPaoDeQueijo[i][j] == 1:
                termo = 9
            else:
                termo = matrizPaoDeQueijo[i-1][j] + matrizPaoDeQueijo[i+1][j] + matrizPaoDeQueijo[i][j-1] + matrizPaoDeQueijo[i][j+1]
            linha.append(termo)
        celula.append(linha)
    return celula



def main():
    while True:
        try:
            n,m = [int(r) for r in input().split()]
            matrizPaoDeQueijo = desenheMatrizPaoDeQueijo(n,m)
            celula = desenheCelula(matrizPaoDeQueijo)
            for linha in celula:
                #print(*linha)
                s = ''
                for i in linha:
                    i = str(i)
                    s += i
                print(s)
        except EOFError:
            break


main()






