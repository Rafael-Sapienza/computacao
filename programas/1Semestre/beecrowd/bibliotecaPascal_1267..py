def simOuNao(N,D):
    matrix = []
    for i in range(D):
        linha = [int(r) for r in input().split()]
        matrix.append(linha)
    flag = [True]*N
    for i in range(len(matrix)):
        for j in range(len(linha)):
            if matrix[i][j] == 0:
                flag[j] = False
    resultado = 'no'
    for item in flag:
        if item:
            resultado = 'yes'
            break
    print(resultado)



def main():
    N,D = [int(r) for r in input().split()]
    while N!=0 and D!=0:
        simOuNao(N,D)
        N,D = [int(r) for r in input().split()]


main()



