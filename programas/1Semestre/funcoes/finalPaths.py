import copy


def find_all_element_in_nested_list(data, element_to_find, index=[]):
    indexes = []
    for i, item in enumerate(data):
        if item == element_to_find:
            indexes.append(index + [i])
        elif isinstance(item, list):
            indexes.extend(find_all_element_in_nested_list(item, element_to_find, index + [i]))
    return indexes


def access_element_by_indices(data, indices):
    try:
        for index in indices:
            data = data[index]
        return data
    except (IndexError, TypeError):
        return None
    


def swapIndexesToRemove(r,indexesToRemove,k):
    #r é uma lista de indices
    indexesToRemove = indexesToRemove[1:]
    indexesToRemove = [indexesToRemove[k]]
    
    i=0
    if len(r) == 1:
        #i=0
        for s in indexesToRemove:
            if s[0] < r[0]:
                pass
            elif s[0] == r[0]:
                indexesToRemove.remove(s)
            else:
                indexesToRemove[i][0] -= 1 
            #i+=1
    else: 
        #i=0
        for s in indexesToRemove:
            if r[:len(r)-1] == s[:len(r)-1]:
                if s[len(r)-1] < r[-1]:
                    pass
                elif s[len(r)-1] == r[-1]:
                    indexesToRemove.remove(s)
                else:
                    indexesToRemove[i][len(r)-1] -= 1 
            #i+=1

    return indexesToRemove



def finalIndexes(r,indexesToRemove):
    x = len(indexesToRemove)
    A=[]
    for k in range(x-1):
        A.extend(swapIndexesToRemove(r,indexesToRemove,k))
    return A




def removeElementsByIndexes(data,indexesToRemove):
    #if indexesToRemove:
    for r in indexesToRemove:
        if len(r)==1:
            data.pop(r[0])
        
        else:
            access_element_by_indices(data, r[:-1]).pop(r[-1])

        indexesToRemove = finalIndexes(r,indexesToRemove)

        if not(indexesToRemove):
            return data
        

    

'''
A= [3,4,['a',[3,8]], 4]

result = find_all_element_in_nested_list(A, [3,8])

B=[2,1,0]

result2 = access_element_by_indices(A, B)

print(result2)

'''


routes = [ [1,2],[2,3],[2,4],[3,5],[4,5] ]

possiblePaths = [ [3] ]


#whereIsIt = [[1, 1], [3, 0]]
#remainingPathsindexes = [1,3]
#remainingPathsindexes = [[1],[3]]


def findFirstPath(routes, possiblePaths):
    
    #global routes, possiblePaths
    
    remainingPathsIndexes = []
    whereIsIt =  find_all_element_in_nested_list(routes, possiblePaths[0][0])
    for r in whereIsIt:
        #externalWhereIsIt = r[:-1]
        remainingPathsIndexes.extend(r[:-1])
        access_element_by_indices(routes, r[:-1]).pop(r[1])
        #routes[externalWhereIsIt].pop(routes[r])

    newPaths=[]
    for r in remainingPathsIndexes:
        B = possiblePaths[0].copy()
        C = B + access_element_by_indices(routes,[r])
        newPaths.append(C)

    remainingPathsIndexes=[[r] for r in remainingPathsIndexes]

    routes = removeElementsByIndexes(data=routes,indexesToRemove=remainingPathsIndexes)

    return [routes,newPaths]

    

newRoutes,newPaths = findFirstPath(routes, possiblePaths)    


'''
routes = [[1, 2], [2, 4], [4, 5]]
possiblePaths = [[3, 2], [3, 5]]
'''

routes = [ [1,2],[2,3],[2,4],[3,5],[4,5] ]

possiblePaths = [[3, 2, 1], [3, 2, 4], [3,5,4]]


def findNthPath(routes,possiblePaths,k=0):
    routes2 = copy.deepcopy(routes)

    possiblePaths = possiblePaths[k] #possiblePaths = [3,2]
    intermidiaryPaths = possiblePaths
    while True:
        r=intermidiaryPaths[0]
        routes2, newPaths = findFirstPath(routes2,[ [r] ])
        intermidiaryPaths = intermidiaryPaths[1:]
        if not(intermidiaryPaths):
            break
    
    if newPaths:   
        D=[]
        for r in newPaths:
            C = possiblePaths + r[1:]
            D.append(C)
        newPaths = D
        
        return newPaths
    
    else:
        return [possiblePaths]



routes = [ [1,2],[2,3],[2,4],[3,5],[4,5] ]

possiblePaths = [[3, 2, 1], [3, 2, 4], [3, 5]]


def findNextPaths(routes, possiblePaths):
    result2 = []
    for k in range(len(possiblePaths)):
        result1 = findNthPath(routes,possiblePaths,k)
        result2.extend(result1)
    newPaths = result2
    return result2




routes = [ [1,2],[2,3],[2,4],[3,5],[4,5] ]

def finalPaths(routes, firstBase = [[3]]):
    paths = findNextPaths(routes = routes, possiblePaths = firstBase)
    while True:
        possiblePaths = paths
        nextPaths = findNextPaths(routes = routes, possiblePaths = possiblePaths)
        possiblePaths = nextPaths
        nextNextPaths = findNextPaths(routes = routes, possiblePaths = possiblePaths)
        paths = nextPaths
        if nextPaths == nextNextPaths:
            return paths
            break


'''
secondPaths= findNextPaths(routes = routes, possiblePaths = firstBase)
print(secondPaths)
possiblePaths = secondPaths
thirdPaths = findNextPaths(routes = routes, possiblePaths = possiblePaths)
print(thirdPaths)
possiblePaths = thirdPaths
fourthPaths = findNextPaths(routes = routes, possiblePaths = possiblePaths)
print(fourthPaths)
possiblePaths = fourthPaths
fithPaths = findNextPaths(routes = routes, possiblePaths = possiblePaths)
print(fithPaths)
possiblePaths = fithPaths
sixthPaths = findNextPaths(routes = routes, possiblePaths = possiblePaths)
print(sixthPaths)
'''


routes = [ [1,2],[2,3],[2,4],[3,5],[4,5] ]


print(finalPaths(routes,firstBase=[[3]]))