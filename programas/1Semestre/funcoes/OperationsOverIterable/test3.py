import copy
from icecream import ic

def changeElementInIndexOfIterable(iterable,index,newElement):
    iterableCopy = copy.deepcopy(iterable)
    currentIterable = iterableCopy
    #Percorra a lista de index de 1 em 1
    for singleIndex in index[:-1]: 
        currentIterable = currentIterable[singleIndex]

    #Atualize o valor do indice final:
    currentIterable[index[-1]] = newElement
    return iterableCopy


def changeElementInIndexOfIterableWithTuples(iterable,index,newElement,flag = 'value',oldKey = 'chaveAntiga'):
    #flag pode ser 'key' ou 'value' a depender se vc quer mudar oo nome de uma chave ou o valor dentro das chaves
    #index eh uma lista que serve tanto para o indice onde uma chave se encotra quanto para o indice onde o valor('value') se encontra
    #newElement pode servir tanto para o novo nome de uma chave quanto para o novo valor dentro de uma chave
    #se index for uma 'iterable', considero que iterable seja um dicionario e que o ususario queira alterar uma das chaves mais externas de iterable
    if index == 'iterable':
        index = [] #fazando isso, pulamos varias linhas dessa funcao e vamos direto a condicao 'if index == []'
    iterableCopy = copy.deepcopy(iterable)
    currentIterable = iterableCopy
    tupleIndex = []
    tupleIndexes = []
    #Percorra a lista de index de 1 em 1
    for i in range(len(index[:-1])-1): 
        singleIndex = index[:-1][i]
        tupleIndex.append(singleIndex)
        currentIterable = currentIterable[singleIndex]
        #Transforme as tuplas em listas para poder modificar o elemento
        proximoIndex = index[:-1][i+1]
        if isinstance(currentIterable[proximoIndex],tuple):
            currentIterable[proximoIndex] = list(currentIterable[proximoIndex])
            #ic(currentIterable)
            #ic(iterableCopy)
            tupleIndex.append(proximoIndex)
            #ic(tupleIndex)
            tupleIndexes.append(tupleIndex)
            #ic(tupleIndexes)
            tupleIndex = tupleIndex[:-1]#esse passo é necessario, pois, na proxima iteracao, tupleIndex vai receber o elemento que perdeu nesse passo. Sem esse passo, esse elemento apareceria de forma duplicada em tupleIndex
    
    #Atualize o valor do indice final:
    try:
        currentIterable = currentIterable[index[-2]] #ainda não iteramos toda lista 'index';so fomos ate i = len(index[:-1])-1. Logo, precisamos executar esse passo
    except IndexError:
        pass
    if flag == 'value':
        currentIterable[index[-1]] = newElement #troca o elemento antigo por um novo elemento
        #ic(iterableCopy)
    elif flag == 'key':
        if index == []: #considero,nesse caso, que o usuário queira alterar uma das chaves na posicao mais externa de iterable(iterable,nesse caso, sera um dicionario)
            iterableCopy[newElement] = iterableCopy.pop(oldKey)
        else:
            currentIterable[index[-1]][newElement] = currentIterable[index[-1]].pop(oldKey) #cria uma nova chave chamada de newElement com o msm valor da chave antiga(oldKey) e remove a chave antiga

    #Transforme de volta em tuplas:
    del tupleIndex
    for tupleIndex in tupleIndexes[::-1]:#Eh necessario percorrer a lista tupleIndex ao contrario, pois eh necessario primeiro transformar os elementos em tuplas nas partes mais internas do objeto iteravel para dps transforma-los fora. Caso contrario, se vc tentar comecar a transformar os elementos em tuplas por fora, vc nao consiguira transforma-los em tuplas dentro,pois tuplas sao objetos imutaveis
        currentIterable = iterableCopy
        for singleIndex in tupleIndex[:-1]:
            currentIterable = currentIterable[singleIndex]
        currentIterable[tupleIndex[-1]] = tuple(currentIterable[tupleIndex[-1]])

    return iterableCopy 







iterable = {
    'casa':{
        'porta':(('maçaneta',0,{'pais':'brasil'}),34)
    },
    'carro':{
        'imposto':{
            'p':2
        },
        'gasolina':456,
    },
}




index = 'iterable'

newElement = 'cidade'

iterable = changeElementInIndexOfIterableWithTuples(iterable,index,newElement,flag = 'key',oldKey = 'casa')

print(iterable)