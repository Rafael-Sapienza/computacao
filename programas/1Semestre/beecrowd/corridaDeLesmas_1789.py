def maiorNívelDasLesmas(lista):
    maiorNível = 0
    for item in lista:
        if item < 10:
            nivel = 1
        elif item>=10 and item<20:
            nivel = 2
        elif item>=20:
            nivel = 3
        if nivel>maiorNível:
            maiorNível = nivel
        if maiorNível == 3:
            break
    print(maiorNível)

def solveProblem():
    while True:
        try:
            x = int(input())
            lista = [int(r) for r in input().split()]
            maiorNívelDasLesmas(lista)
        except EOFError:
            break

solveProblem()