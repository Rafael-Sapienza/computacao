from icecream import ic


dictionary = {
    'casa':{
        'b':[0,1]},
    'mesa':[12]
}

lista = [1,2,3,4,5]
lista2 = lista[::-2]
ic(lista2)

def accessElementByIndexInIterable(iterable,index):
    for i in index:
        iterable = iterable[i]
    return iterable


print(accessElementByIndexInIterable(iterable=dictionary,index = ['casa']))