def makeDict(M):
    pontosDeFeno = {}
    for _ in range(M):
        key,value = [r for r in input().split()]
        value = int(value)
        pontosDeFeno[key] = value
    return pontosDeFeno

def quantoRecebeCadaUm(pontosDeFeno):
    s = ''
    s2 = input()
    while s2 != '.':
        s += s2 + ' '
        s2 = input()
    L = s.split()
    counter = 0
    for item in L:
        if item in pontosDeFeno:
            counter += pontosDeFeno[item]
    return counter

def main():
    M, N = [int(r) for r in input().split()]
    pontosDeFeno = makeDict(M)
    for _ in range(N):
        salario = quantoRecebeCadaUm(pontosDeFeno)
        print(salario)

main()



