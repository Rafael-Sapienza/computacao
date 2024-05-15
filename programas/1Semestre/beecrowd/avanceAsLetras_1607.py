def numeroMinDeOperacoes(s1,s2):
    numeroMinDeOperacoes = 0
    for i in range(len(s1)):
        elemento1 = s1[i]
        elemento2 = s2 [i]
        codigoAsc1 = ord(elemento1)
        codigoAsc2 = ord(elemento2)
        codigoAsc1 -= 97
        codigoAsc2 -= 97
        numeroMinDeOperacoesPorCaracter = codigoAsc2 - codigoAsc1
        numeroMinDeOperacoesPorCaracter = numeroMinDeOperacoesPorCaracter%26
        numeroMinDeOperacoes += numeroMinDeOperacoesPorCaracter
    return numeroMinDeOperacoes

def printAllNumeroMinDeOperacoes(N):
    for _ in range(N):
        s1,s2 = input().split()
        x = numeroMinDeOperacoes(s1,s2)
        print(x)

N = int(input())
printAllNumeroMinDeOperacoes(N)

