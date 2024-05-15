def makeMatrix():
    matrix = []
    for i in range(12):
        linha = []
        for j in range(12):
            x = float(input())
            linha.append(x)
        matrix.append(linha)
    return matrix

def calculeOperacaoSobreMatriz(matrix,operacao):
    soma = 0
    counter = 0
    for i in range(12):
        for j in range(i+1,12):
            soma += matrix[i][j]
            counter += 1
    if operacao == 'S':
        return soma
    else:
        media = soma/counter
        return media





operacao = input()
matrix = makeMatrix()
resultado = calculeOperacaoSobreMatriz(matrix,operacao)
print(f'{resultado:.1f}')