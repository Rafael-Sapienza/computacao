import copy
from icecream import ic 
def accessElementByIndices(data, indices):
    try:
        for index in indices:
            data = data[index]
        return data
    except (IndexError, TypeError):
        return None
    
'''
if len(index)>1:
    accessElementByIndices(data=data,indices = index[:-1]) = accessElementByIndices(data=data, indices=index[:-1])[:index[-1]] + [element] + accessElementByIndices(data=data, indices=index[:-1])[index[-1]:]
else:
    data = data[:index[0]] + [element] + data[index[0]:]
'''


data = [1,2,[5,6],3]
index = [2,1]
element = 'a'

A = accessElementByIndices(data=data, indices=index[:-1])[:index[-1]] + [element] + accessElementByIndices(data=data, indices=index[:-1])[index[-1]:]
dataCopy = copy.deepcopy(data)
accessElementByIndices(data=data,indices = index[:-1])
print(A)
print(data)