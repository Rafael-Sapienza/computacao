import copy
#INPUTS:

def getInputs():
    firstInputs=[int(r) for r in input().split()]
    N , M, D = firstInputs

    secondInputs = []
    for _ in range(M):
        secondInputs.append([int(r) for r in input().split()])

    routes = []
    for i in range(len(secondInputs)):
        routes.append(secondInputs[i][0:2])


    tempos=[]
    for i in range(len(secondInputs)):
        tempos.append(secondInputs[i][2])

    return [N,M,D,routes,tempos]




#FUNCOES UTEIS:

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
    data1 = copy.deepcopy(data)
    for r in indexesToRemove:
        if len(r)==1:
            data1.pop(r[0])
        
        else:
            access_element_by_indices(data1, r[:-1]).pop(r[-1])

        indexesToRemove = finalIndexes(r,indexesToRemove)

        if not(indexesToRemove):
            return data1
        

    
#CAMINHOS:

def findFirstPath(routes, possiblePaths):
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
   

'''
routes = [[1, 2], [2, 4], [4, 5]]
possiblePaths = [[3, 2], [3, 5]]
'''

def findNthPath(routes,possiblePaths,k):
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


def findNextPaths(routes, possiblePaths):
    result2 = []
    for k in range(len(possiblePaths)):
        result1 = findNthPath(routes,possiblePaths,k)
        result2.extend(result1)
    newPaths = result2
    return result2


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

#N=número de bases
#M é o número de trilhas
#D é a posicao do disco voador

def findIndexesMinimumNumberInList(A):
    B=[0]
    for i in range(len(A)):
        C = B.copy()
        if A[i]<A[B[0]]:
            B = [i]
        if i != 0:
            if A[i] == A[C[0]]:
                B.extend([i])
    return B

def findElementsWithLeastLenght(list):
    A=[]
    for r in list:  #r is a list
        A.append(len(r))
    indexesMinimumNumbers = findIndexesMinimumNumberInList(A)
    D=[]
    for i in indexesMinimumNumbers:
        D.append(list[i])
    return D

def caminhosDeAristenio(routes,N, D=1):
    todosCaminhosAristenio = finalPaths(routes, firstBase = [[D]])
    caminhosPossiveisAristenio = []
    whereIsLastBase = find_all_element_in_nested_list(data=todosCaminhosAristenio,element_to_find=N)
    for r in whereIsLastBase:
        F = todosCaminhosAristenio[r[:-1][0]]
        caminhosPossiveisAristenio.append(F[:r[-1]+1])
    return caminhosPossiveisAristenio


def caminhosDeDisco(routes,N, D):
    caminhosPossiveisDisco = caminhosDeAristenio(routes,N, D)
    return caminhosPossiveisDisco

#TODOS OS TEMPOS:

def helpFindTimeOfRoute(trilha):
    A=[]
    i=0
    while i <= len(trilha)-2:
        A.append(trilha[i:i+2])
        i+=1
    return A

def getTimeFromRoute(whichRoute, routes, tempos):
    for i in range(len(routes)):
        if whichRoute == routes[i] or [whichRoute[1],whichRoute[0]] == routes[i]:
            return tempos[i]
        else:
            pass

def tempoDaTrilha(routes, tempos, trilha):
    tempo = 0
    for r in helpFindTimeOfRoute(trilha):
        tempo += getTimeFromRoute(whichRoute = r, routes= routes, tempos = tempos)
    return tempo


def temposAristenio(caminhosPossiveisAristenio,routes,tempos):
    TEMPOS = []
    for r in caminhosPossiveisAristenio:
        TEMPOS.append(tempoDaTrilha(routes, tempos, trilha=r))
    return TEMPOS

def temposDisco(caminhosPossiveisDisco):
    TEMPOS = []
    for r in caminhosPossiveisDisco:
        trilha = helpFindTimeOfRoute(trilha = r)
        tempoTrilha = len(trilha)
        TEMPOS.append(tempoTrilha)
    return TEMPOS


def willAristenioWin(temposDoAristenio, temposDoDisco):
    A = copy.deepcopy(temposDoAristenio)
    B = copy.deepcopy(temposDoDisco)   
    A.sort()
    B.sort()  
    if A[0] < B[0]:
        return 'SIM'
    else:
        return 'NAO'


#CHAMADAS FUNCOES:

N,M,D,routes,tempos = getInputs()

caminhosPossiveisAristenio = caminhosDeAristenio(routes,N, D=1)
caminhosPossiveisDisco = caminhosDeDisco(routes,N, D)

temposDoAristenio = temposAristenio(caminhosPossiveisAristenio,routes,tempos)
temposDoDisco = temposDisco(caminhosPossiveisDisco)

finalResult = willAristenioWin(temposDoAristenio, temposDoDisco)


print('caminhosPossiveisAristenio:', caminhosPossiveisAristenio)
print('caminhosPossiveisDisco:', caminhosPossiveisDisco)
print('temposDoAristenio:' , temposDoAristenio)
print('temposDoDisco:' , temposDoDisco)


print('finalResult:' , finalResult)