def mostreNotaDaCompetidora(competidora,grauDeDificuldade,L):
    nota = 0
    for item in L:
        nota += item
    nota = nota - min(L) - max(L)
    nota *= grauDeDificuldade
    print(f'{competidora} {nota:.2f}')




def solveMyProblem(N):
    for i in range(N):
        competidora = input()
        grauDeDificuldade = float(input())
        L = [float(r) for r in input().split()]
        mostreNotaDaCompetidora(competidora,grauDeDificuldade,L)

N = int(input())
solveMyProblem(N)