def makeDict():
    myDict = {}
    N = int(input())
    for _ in range(N):
            n = int(input())
            if n not in myDict:
                myDict[n] = 1
            else:
                myDict[n] += 1
    return myDict

def printValue(myDict):
    L = sorted(myDict)
    for item in L:
        print(f'{item} aparece {myDict[item]} vez(es)')

myDict = makeDict()
printValue(myDict)