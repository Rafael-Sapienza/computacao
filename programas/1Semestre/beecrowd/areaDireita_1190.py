def makeMatrix():
    matrix = []
    for i in range(12):
        linha = []
        for j in range(12):
            x = float(input())
            linha.append(x)
        matrix.append(linha)
    return matrix


def calculeOperacao(operacao,matrix):
    soma = 0
    counter = 0
    for i in range(6):
        for j in range(12-i,12):
            soma += matrix[i][j]
            counter += 1
    for i in range(6,12):
        for j in range(7+i%6,12):
            soma += matrix[i][j]
            counter += 1
    if operacao == 'S':
        return soma
    else:
        media = soma/counter
        return media



operacao = input()
matrix = makeMatrix()
result = calculeOperacao(operacao,matrix)
print(f'{result:.1f}')