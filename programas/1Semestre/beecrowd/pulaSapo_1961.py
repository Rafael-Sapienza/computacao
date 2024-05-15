def solveProblem():
    flag = True
    P,N = [int(r) for r in input().split()]
    L = [int(r) for r in input().split()]
    for i in range(N-1):
        item1 = L[i]
        item2 = L[i+1]
        dif = item2 - item1
        if abs(dif) > P:
            flag = False
            break
    if flag:
        print('YOU WIN')
    else:
        print('GAME OVER')


solveProblem()