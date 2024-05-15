import copy
from icecream import ic 

def accessElementByIndices(data, indices):
    try:
        for index in indices:
            data = data[index]
        return data
    except (IndexError, TypeError):
        return None


def swapKthIndex(indexes,k):
    lastInsertedElementPosition = copy.deepcopy(indexes[0])
    index = copy.deepcopy(indexes[k])
    if len(lastInsertedElementPosition) <= len(index):
        if len(lastInsertedElementPosition) == 1:
            if index[0] < lastInsertedElementPosition[0]:
                pass
            else:
                index[0]+=1
        elif lastInsertedElementPosition[:-1] == index[:len(lastInsertedElementPosition)-1]:
            if index[len(lastInsertedElementPosition)-1] < lastInsertedElementPosition[-1]:
                pass
            else:
                index[len(lastInsertedElementPosition)-1] += 1
    else:
        pass
    return index


def swapIndexes(indexes):
    for k in range(1,len(indexes)):
        indexes[k] = swapKthIndex(indexes,k)
    indexes = indexes[1:]
    return indexes

def insertElementByIndexes(data, element, indexes):
    while True:  
        index = indexes[0]
        if(len(index))>1:
            accessElementByIndices(data=data,indices = index[:-1]).insert(index[-1],element)
        else:
            data.insert(index[0], element)
        indexes = swapIndexes(indexes)
        if not(indexes):
            return data
            break
    

data=[2,[4,5]]
element='a'
indexes=[[1],[2]]
ic(insertElementByIndexes(data, element, indexes))