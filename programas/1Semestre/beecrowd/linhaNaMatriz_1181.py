def makeMatrix():
    matrix = []
    linha = []
    for i in range(12):
        linha = []
        for j in range(12):
            x = float(input())
            linha.append(x)
        matrix.append(linha)
    return matrix

def facaOsCalculos(matrix,n,operacao):
    if operacao == 'S':
        soma = 0
        for i in matrix[n]:
            soma += i
        return soma
    if operacao == 'M':
        soma = 0
        for i in matrix[n]:
            soma += i
        media = soma/12
        return media


n = int(input())
operacao = input()
matrix = makeMatrix()
resultado = facaOsCalculos(matrix,n,operacao)
print(f'{resultado:.1f}')