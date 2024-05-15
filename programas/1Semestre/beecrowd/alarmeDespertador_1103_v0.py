def minutosDeSono(h1,m1,h2,m2):
    minutosInicial = 60*h1 + m1
    minutosFinal = 60*h2 + m2
    if minutosFinal < minutosInicial:
        minutosFinal += 24*60
    minutosTotal = minutosFinal - minutosInicial
    print(minutosTotal)


def solveProblem():
    while True:
        A = [int(r) for r in input().split()]
        h1,m1,h2,m2 = A
        if A == [0,0,0,0]:
            break
        minutosDeSono(h1,m1,h2,m2)
        
 
        
solveProblem()
