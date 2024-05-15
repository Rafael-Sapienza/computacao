#from operationsOverLists.removeElementsByIndexes import removeElementsByIndexes
import sys
sys.path.insert(1,'C://Users//rafae//Rafael_Mateus//Rafael//UNB//programas//funcoes//operationsOverLists')
import removeElementByIndexes
import copy
from icecream import ic 

def accessElementByIndices(data, indices):
    try:
        for index in indices:
            data = data[index]
        return data
    except (IndexError, TypeError):
        return None


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

def insertElementByIndexes2(data, element, indexes):
    indexesCopy = copy.deepcopy(indexes)
    while True:
        index = indexesCopy[0]
        if(len(index))>1:
            accessElementByIndices(data=data,indices = index[:-1]).insert(index[-1],element)
        else:
            data.insert(index[0], element)
        indexesCopy = indexesCopy[1:]
        if not(indexesCopy):
            return data
            break

def replaceElementsByIndexes(data, newElement, indexes):
    newData = removeElementsByIndexes(data,indexes)
    data = newData
    newData = insertElementByIndexes2(data, newElement, indexes)
    data = newData
    return data



data=[1,[5,6],[2,3,5]]
element='abc'
indexes=[[1,0],[2,1]]
result = replaceElementsByIndexes(data,element, indexes)
ic(result)
