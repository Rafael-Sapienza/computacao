import copy
from icecream import ic


def getInput():
    numeroTocas, numeroAnalises = [int(r) for r in input().split()]
    burrowConnections = []
    burrowWidths = []
    for r in range(numeroTocas-1):
        A = [int(r) for r in input().split()]
        burrowConnections.append(A[:2])
        burrowWidths.append(A[2])
    objetosDeAnalise = []
    for r in range(numeroAnalises):
        objetosDeAnalise.append([int(r) for r in input().split()])
    return burrowConnections, burrowWidths, objetosDeAnalise


def accessElementByIndices(data, indices):
        try:
            for index in indices:
                data = data[index]
            return data
        except (IndexError, TypeError):
            return None   


def findAllElementInNestedList(data, elementToFind, index=[]):
    indexes = []
    for i, item in enumerate(data): 
        if item == elementToFind:
            indexes.append(index + [i])
        elif isinstance(item, list):
            indexes.extend(findAllElementInNestedList(item, elementToFind, index + [i]))
    return indexes


def removeElementsByIndexes(data,indexesToRemove): 
    def finalIndexes(r,indexesToRemove):
        def swapIndexesToRemove(r,indexesToRemove,k):
            indexesToRemoveCopy = copy.deepcopy(indexesToRemove)
            indexesToRemoveCopy = indexesToRemoveCopy[1:]
            indexesToRemoveCopy = [indexesToRemoveCopy[k]]
            
            i=0
            if len(r) == 1:
                for s in indexesToRemoveCopy:
                    if s[0] < r[0]:
                        pass
                    elif s[0] == r[0]:
                        indexesToRemoveCopy.remove(s)
                    else:
                        indexesToRemoveCopy[i][0] -= 1 
            else: 
                for s in indexesToRemoveCopy:
                    if r[:len(r)-1] == s[:len(r)-1]:
                        if s[len(r)-1] < r[-1]:
                            pass
                        elif s[len(r)-1] == r[-1]:
                            indexesToRemoveCopy.remove(s)
                        else:
                            indexesToRemoveCopy[i][len(r)-1] -= 1 

            return indexesToRemoveCopy

        x = len(indexesToRemove)
        A=[]
        for k in range(x-1):
            A.extend(swapIndexesToRemove(r,indexesToRemove,k))
        return A

    data1 = copy.deepcopy(data)
    while True:
        r = indexesToRemove[0]
        if len(r)==1:
            data1.pop(r[0])
        
        else:
            accessElementByIndices(data1, r[:-1]).pop(r[-1])

        indexesToRemove = finalIndexes(r,indexesToRemove)

        if not(indexesToRemove):
            return data1        
            break


def removePastBurrow(burrowConnections,pastBurrow):
    if burrowConnections:
        lastBurrowIndexes = findAllElementInNestedList(data = burrowConnections, elementToFind = pastBurrow)
        if lastBurrowIndexes:
            burrowConnectionsCopy = removeElementsByIndexes(data=burrowConnections, indexesToRemove=lastBurrowIndexes)
            nextBurrows = []
            for index in lastBurrowIndexes:
                nextBurrows.append(accessElementByIndices(data = burrowConnectionsCopy, indices = index[:-1] + [0]))
            newIndexesToRemove = []
            for r in lastBurrowIndexes:
                newIndexesToRemove.append(r[:-1])
            burrowConnectionsCopy = removeElementsByIndexes(data = burrowConnectionsCopy, indexesToRemove=newIndexesToRemove)
        else:
            nextBurrows = []
            burrowConnectionsCopy = []
    else:
        nextBurrows = []
        burrowConnectionsCopy=[]
    return nextBurrows, burrowConnectionsCopy


def findNextPathesBasedOnOnePath(burrowConnections, path=[3,6,10,1]):
    for pastBurrow in path[:-1]:
        burrowConnections = removePastBurrow(burrowConnections,pastBurrow)[1]
    nextBurrows = removePastBurrow(burrowConnections,path[-1])[0]
    pathes = []
    for i in nextBurrows:
        pathes = pathes + [path+[i]]
    if pathes:
        pass
    else:
        pathes = [path]
    return pathes


def findNextPathesBasedOnHoweverManyPathes(burrowConnections, pathes=[[3,6],[3,9]]):
    nextPathes = []
    for path in pathes:
        L = findNextPathesBasedOnOnePath(burrowConnections, path)
        nextPathes.extend(L)
    return nextPathes


def findAllPathes(burrowConnections, beginning=3):
    nextPathes = [[beginning]]
    while True:
        inicialPathes = nextPathes
        nextPathes = findNextPathesBasedOnHoweverManyPathes(burrowConnections, nextPathes)
        if inicialPathes == nextPathes:
            return nextPathes
            break 


def treatFinalPathes(allPathes, ending):
    finalPathes=[]
    for r in allPathes:
        if ending in r:
            finalPathes.append(r[:r.index(ending)+1])
    return finalPathes


def findFinalPathes(burrowConnections, beginning, ending):
    allPathes = findAllPathes(burrowConnections, beginning)
    finalPathes = treatFinalPathes(allPathes, ending)
    return finalPathes


def findAllFinalPathes(burrowConnections, objetosDeAnalise):
    L=[]
    for r in objetosDeAnalise:
        beginning = r[0]
        ending = r[1]
        L.extend(findFinalPathes(burrowConnections, beginning, ending))
    return L


def findWidthForPairOfBurrows(pair,burrowConnections, burrowWidths):
    for i in range(len(burrowConnections)):
        if pair == burrowConnections[i] or [pair[1],pair[0]]==burrowConnections[i]:
            result = burrowWidths[i]
            return result


def findWidthOfKthIndexPath(allPathes,burrowConnections, burrowWidths, k):
    kthPath = allPathes[k]
    width = 0
    for i in range(len(kthPath)-1):
        pair = kthPath[i:i+2]
        width += findWidthForPairOfBurrows(pair,burrowConnections, burrowWidths)
    return width


def findWidthsOfAllPathes(allPathes,burrowConnections, burrowWidths):
    widths = []
    for k in range(len(allPathes)):
        widths.append(findWidthOfKthIndexPath(allPathes,burrowConnections, burrowWidths, k))
    return widths


def printResult(widthsOfAllPathes):
    for i in widthsOfAllPathes:
        print(i)


'''
burrowConnections = [[10,1],[6,10],[3,6],[9,3],[2,3],[11,3],[11,7],[11,5],[11,4],[8,11]]
burrowWidths = [5, 3, 8, 5, 7, 10, 2, 1, 4, 6]
objetosDeAnalise = [[1,5],[11,7],[6,8],[9,2]]
'''

burrowConnections, burrowWidths, objetosDeAnalise = getInput()
ic(burrowConnections, burrowWidths, objetosDeAnalise)


allPathes = findAllFinalPathes(burrowConnections, objetosDeAnalise)
ic(allPathes)


widthsOfAllPathes = findWidthsOfAllPathes(allPathes,burrowConnections, burrowWidths)
ic(widthsOfAllPathes)


printResult(widthsOfAllPathes)