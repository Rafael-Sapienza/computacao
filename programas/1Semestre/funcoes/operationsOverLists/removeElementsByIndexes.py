import copy


def access_element_by_indices(data, indices):
    try:
        for index in indices:
            data = data[index]
        return data
    except (IndexError, TypeError):
        return None



def swapIndexesToRemove(r,indexesToRemove,k):
    #r é uma lista de indices
    indexesToRemoveCopy = copy.deepcopy(indexesToRemove)
    indexesToRemoveCopy = indexesToRemoveCopy[1:]
    indexesToRemoveCopy = [indexesToRemoveCopy[k]]
    
    i=0
    if len(r) == 1:
        #i=0
        for s in indexesToRemoveCopy:
            if s[0] < r[0]:
                pass
            elif s[0] == r[0]:
                indexesToRemoveCopy.remove(s)
            else:
                indexesToRemoveCopy[i][0] -= 1 
            #i+=1
    else: 
        #i=0
        for s in indexesToRemoveCopy:
            if r[:len(r)-1] == s[:len(r)-1]:
                if s[len(r)-1] < r[-1]:
                    pass
                elif s[len(r)-1] == r[-1]:
                    indexesToRemoveCopy.remove(s)
                else:
                    indexesToRemoveCopy[i][len(r)-1] -= 1 
            #i+=1

    return indexesToRemoveCopy



def finalIndexes(r,indexesToRemove):
    x = len(indexesToRemove)
    A=[]
    for k in range(x-1):
        A.extend(swapIndexesToRemove(r,indexesToRemove,k))
    return A




def removeElementsByIndexes(data,indexesToRemove):
    #if indexesToRemove:
    data1 = copy.deepcopy(data)
    #for r in indexesToRemove:
    while True:
        r = indexesToRemove[0]
        if len(r)==1:
            data1.pop(r[0])
        
        else:
            access_element_by_indices(data1, r[:-1]).pop(r[-1])

        indexesToRemove = finalIndexes(r,indexesToRemove)

        if not(indexesToRemove):
            return data1        
            break
'''
A = [['a', 'b'], ['c', 'd', 'e'], ['f', 'g', 'h', 'i']]
B = [[0], [1, 1], [2]]
'''

'''
A=[2,2,[1,0]]
B=[[1],[2,1]]
'''

'''
print(removeElementsByIndexes(data=A,indexesToRemove=B))
#print(B)
'''