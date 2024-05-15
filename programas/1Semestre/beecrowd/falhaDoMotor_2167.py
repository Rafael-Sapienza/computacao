def solveMyProblemPlease():
    flag = False
    N = int(input())
    L = [int(r) for r in input().split()]
    for i in range(N-1):
        item1 = L[i]
        item2 = L[i+1]
        if item2<item1:
            print(i+2)
            flag = True
            break
    if not(flag):
        print(0)



solveMyProblemPlease()
