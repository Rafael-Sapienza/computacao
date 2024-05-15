import copy
from icecream import ic



def findElementInIterable(iterable,element,index = [], indexes = [],keyIndexes = [],flag = None):
    if flag == 'keys':
        if iterable == element:
            indexCopy = copy.deepcopy(index)
            keyIndexes.append(indexCopy)
            return index,indexes,keyIndexes
        elif not(isinstance(iterable,(dict,tuple,list))):
            return index,indexes,keyIndexes
    elif flag == 'values':
        if iterable == element:
            indexCopy = copy.deepcopy(index)
            indexes.append(indexCopy)
            index = index[:-1]
            return index,indexes,keyIndexes
        elif not(isinstance(iterable,(dict,tuple,list))):
            index = index[:-1]
            return index,indexes,keyIndexes
    if isinstance(iterable,dict):
        flag = 'keys'
        for key in iterable.keys():
            #index.append(key)
            index,indexes,keyIndexes = findElementInIterable(key,element,index,indexes,keyIndexes,flag)
        flag = 'values'
        for key,value in iterable.items():
            index.append(key)
            index,indexes,keyIndexes = findElementInIterable(value,element,index,indexes,keyIndexes,flag)
        index = index[:-1]
        return index,indexes,keyIndexes
    elif isinstance(iterable,(list,tuple)):
        for i, item in enumerate(iterable):
            index.append(i)
            index, indexes,keyIndexes = findElementInIterable(item,element,index,indexes,keyIndexes,flag)
        index = index[:-1]
        return index,indexes,keyIndexes
            
        

'''def isElementAnOuterKeyInDictionary(dictionary,element): #descobre se a chave(element) que estamos procurando está na parte mais externa do dicionario
    index = []
    for key in dictionary.keys():
        if key == element:
            index.append('iterable')
            break
    return index'''


def findAllElementInIterable(iterable,element): 
    index,indexes,keyIndexes = findElementInIterable(iterable,element,index = [], indexes = [],keyIndexes = [],flag = None)
    #Se houver uma outerKey com o nome do elemento que procuramos, a funcao findElementInIterable farah keyIndexes appendar []. Essa lista vazia será appendada no maximo uma vez, pois se uma chave outerKey for o elemento que procuramos, nao havera outra chave outerKey de msm nome, pois duas chaves diferentes de um dicionario nao podem ter msm nome(do contrario, uma eh desconsiderada).Ademais, se houver uma outerKey com o nome do elemento que procuramos, o [] serah o primeiro elemento a ser appendado por keyIndexes, pois finndElementInIterable eh uma funcao que passa primeiro por todas as chaves de um dicionario para, dps, passar pelos seus valores. Assim, se houver essa outerKey, ela serah o primeiro elemento a ser encontrado
    if keyIndexes:
        if keyIndexes[0] == []:
            keyIndexes[0] = 'iterable'
    return indexes,keyIndexes







'''
myDict =  {
     'carro':{
          'pintura': 'i',
          'imposto':23,
          'gasolina':24,
}
}'''


'''
myDict = [
    [{'casa':[2,3,'b'],
     'milho':'verde',
     'arroz':(1,4,'b')
     }],
     ['a','b']
]'''


myDict = {
    'casa':{
        'carro':{
            'a':{'carro':True},
            'b':'carro',
                },    
        'carrot': (0,9,['b',1,2],3,4),
},
    'carro':['a','b',[204]],
    'pedagio':34
}

iterable = myDict
element = 'carro'
#index,indexes,keyIndexes = findElementInIterable(iterable,element)
#ic(indexes,keyIndexes)

indexes,keyIndexes = findAllElementInIterable(iterable,element)
ic(indexes,keyIndexes)
