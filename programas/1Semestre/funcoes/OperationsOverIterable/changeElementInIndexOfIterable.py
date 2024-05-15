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


def changeElementInIndexOfIterableWithTuples(iterable,index,newElement,flag = 'value',oldKey = None):
    #flag pode ser 'key' ou 'value', a depender se vc quer mudar oo nome de uma chave ou o valor dentro das chaves
    #index eh uma lista que serve tanto para o indice onde uma chave se encotra quanto para o indice onde o valor('value') se encontra
    #newElement pode servir tanto para o novo nome de uma chave quanto para o novo valor dentro de uma chave
    #se index for uma 'iterable', considero que iterable seja um dicionario e que o ususario queira alterar uma das chaves mais externas de iterable
    #se index for uma lista vazia no inicio, queremmos que a funcao nao altere nenhum termo do iterable
    if index == []:
        return iterable
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



'''def treatIndexesAndKeyIndexes(flag,indexes,keyIndexes):
    Valido = True
    if flag == 'values':
        if indexes != ['iterable']*len(indexes):
            for i in range(len(indexes)-1):
                if len(indexes[i]) != len(indexes[i+1]):
                    valido = False
                    break
    if '''







def changeMultipleIndexesOfIterable(iterable,indexes,newValues,flag0 = 'valores', flag1 = 'unicoNewValue',flag2 = 'unicaNewKey',keyIndexes = [[]],oldKeys = None,newKeys = None):
    # flag0 determina se queremos mudar os valores ou as chaves dentro de iterable. Nao podemos mudar os dois ao mesmo tempo, pois, ao mudarmos os valores, podemos acabar apagando a posicao onde estavam os inidces de keyIndexes, o que tornaria impossivel renomear as chaves nesses pontos

    # se flag1 == 'unicoNewValue', considero que o usuario queira que newValues seja unico, ou seja, msm que newValues seja uma lista, considero que todos os indices em indexes devam receber essa lista. Por exemplo, seja flag = 'unicoNewValue', indexes = [['casa','parede'],['carro',0]] e newValues = [True,(macaneta,{'gasolina':cara})]. Entao, quero que iterable['casa']['parede'] = newValues e que iterable['carro'][0] = newValues

    # se flag1 == 'multiplosNewValues', entao newValues serah uma lista de novos valores, que devem ser posicionados nos indices na ordem que eles aparecem em indexes. Por exemplo, seja indexes = [['casa','parede'],['carro',0]] e newValues = [True,(macaneta,{'gasolina':cara})]. Entao, quero que iterable['casa']['parede'] = True e que iterable['carro'][0] = (macaneta,{'gasolina':cara}). Quando flag1 == 'multiplosNewValues, naturalmente, deveremos ter len(indexes) = len(newValues)

    # oldKeys é uma lista de chaves antigas que serao substituidas pelas novas chaves. Naturalmente, como cada chave antiga estah relacionada em um indice em keyIndexes, len(keyIndexes) = len(oldKeys)

    #se flag2 == 'unicaNewKey', considero que todos os indices em keyIndexes receberao a msm chave
    
    #se flag2 == 'multiplasNewKeys', considero que newKeys serah uma lista de novos valores que devem ser inseridos em interable de acordo com a ordem dos indices em keyIndexes. Quando isso ocorrer, naturalmente, deveremos ter len(keyIndexes) = len(newKeys)

    #se indexes for [[]], os valores de newIterable serao os msms que os de iterable
    #se keyIndexes for [[]], as chaves de newIterable serao as msms que as de iterable
    try:
        newIterable = copy.deepcopy(iterable)
        if flag0 == 'valores':
            if flag1 == 'unicoNewValue':
                for index in indexes:
                    newIterable = changeElementInIndexOfIterableWithTuples(newIterable,index,newValues,flag = 'value',oldKey = None)
            elif flag1 == 'multiplosNewValues':
                for i in range(len(indexes)):
                    index = indexes[i]
                    singleNewValue = newValues[i]
                    newIterable = changeElementInIndexOfIterableWithTuples(newIterable,index,singleNewValue,flag = 'value',oldKey = None)
        elif flag0 == 'chaves':
            if flag2 == 'unicaNewKey':
                for i in range(len(keyIndexes)):
                    keyIndex = keyIndexes[i]
                    singleOldKey = oldKeys[i]
                    newIterable = changeElementInIndexOfIterableWithTuples(newIterable,keyIndex,newKeys,flag = 'key',oldKey = singleOldKey)
            elif flag2 == 'multiplasNewKeys':
                for i in range(len(keyIndexes)):
                    keyIndex = keyIndexes[i]
                    singleOldKey = oldKeys[i]
                    singleNewKey = newKeys[i]
                    newIterable = changeElementInIndexOfIterableWithTuples(newIterable,keyIndex,singleNewKey,flag = 'key',oldKey = singleOldKey)
    except (IndexError,TypeError,KeyError):
        #TypeError ocorre quando tenta-se acessar uma lista com uma chave
        #KeyError ocorre quando tenta-se accessar um dicionario com um indice de lista(um inteiro noo lugar de string) ou quando tenta-se acessar uma chave que nao existe em um dicionario
        print('indices invalidos')
        return None
    return newIterable
    


iterable = {
    'casa':{
        'porta':(['maçaneta',0],34),
        'parede':{
            'tinta':['azul','branco'],
            'material':['concreto']
        }
    },
    'carro':{
        'imposto':123,
        'gasolina':456,
    },
}



'''
newElement = True

flag = 'value'

oldKey = 'imposto'


iterable = changeElementInIndexOfIterableWithTuples(iterable,index,newElement,flag,oldKey)

ic(iterable)
'''

indexes = [['carro'],['carro','imposto'],['casa','porta',0,0],['casa','porta',1]]

newValues = [[1,2],True,(None),0]

keyIndexes = [['casa','parede'],['carro']] #funciona com 'iterable' tbm

oldKeys = ['tinta','imposto']

newKeys = ['pintura','taxacao']

valueIterable = changeMultipleIndexesOfIterable(iterable,indexes,newValues,flag0 = 'valores', flag1 = 'multiplosNewValues',flag2 = 'unicaNewKey',keyIndexes = [[]],oldKeys = None,newKeys = None)

ic(valueIterable)

keyIterable = changeMultipleIndexesOfIterable(iterable,indexes,newValues,flag0 = 'chaves', flag1 = 'multiplosNewValues',flag2 = 'multiplasNewKeys',keyIndexes = keyIndexes,oldKeys = oldKeys,newKeys = newKeys)

ic(keyIterable)