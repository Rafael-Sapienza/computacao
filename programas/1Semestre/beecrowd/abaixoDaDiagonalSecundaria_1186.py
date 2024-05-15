def makeMatrix():
    matrix = []
    for i in range(12):
        linha = []
        for j in range(12):
            x = float(input())
            linha.append(x)
        matrix.append(linha)
    return matrix


def calule(operacao, matrix):
    soma = 0
    counter = 0
    for i in range(12):
        for j in range(12-i,12):
            soma += matrix[i][j]
            counter += 1
    if operacao == 'S':
        return soma
    else:
        media = soma/counter
        return media



operacao = input()
matrix = makeMatrix()
resultado = calule(operacao, matrix)
print(f'{resultado:.1f}')