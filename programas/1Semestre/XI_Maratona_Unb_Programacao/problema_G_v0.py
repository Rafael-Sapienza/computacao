from icecream import ic 
import copy
#funcoes:
def getInput():
    tamanhoStrings = int(input())
    s = input()
    t = input()
    return tamanhoStrings, s, t

def makeStringList(tamanhoStrings, s,t):
    listaDeStrings= []
    for i in range(tamanhoStrings):
        relacao = [s[i],t[i]]
        listaDeStrings.append(relacao)
    return listaDeStrings

#ic(makeStringList(tamanhoStrings, s,t))

def removeRepetitiveElements(listaDeStrings):
    listaDeStringsCopy = copy.deepcopy(listaDeStrings)
    i = 0
    while i < len(listaDeStringsCopy):
        if listaDeStringsCopy[i][0] == listaDeStringsCopy[i][1]:
            listaDeStringsCopy.pop(i)
        i+=1
    return listaDeStringsCopy

def isItPossibleToMakeString(listaDeStrings):
    result = True
    for i in range(len(listaDeStrings)):
        for j in range(len(listaDeStrings)):
                if i != j and listaDeStrings[i][0] == listaDeStrings[j][0]:
                    if listaDeStrings[i][1] != listaDeStrings[j][1]:
                        result = False
    return result

def treatListaDeStrings(listaDeStrings):
    listaDeStringsCopy = copy.deepcopy(listaDeStrings)
    i = 0
    while i < len(listaDeStringsCopy):
        j=0
        while j < len(listaDeStringsCopy):
            if i != j:
                    if listaDeStringsCopy[i] == listaDeStringsCopy[j]:
                        listaDeStringsCopy.pop(j)
            j+=1
        i+=1    
                
    return listaDeStringsCopy


def calculateNumberOfSwaps(listaDeStrings):
    if isItPossibleToMakeString(listaDeStrings):
        x = 0
        for i in range(len(listaDeStrings)):
            if listaDeStrings[i][0] != listaDeStrings[i][1]:
                x += 1
        return x
    else:
        return -1
               
#variaveis globais:

tamanhoStrings, s, t = getInput()
listaDeStrings = makeStringList(tamanhoStrings, s,t)
listaDeStrings = removeRepetitiveElements(listaDeStrings)
ic(listaDeStrings)
listaDeStrings = treatListaDeStrings(listaDeStrings)
ic(listaDeStrings)

ic(isItPossibleToMakeString(listaDeStrings))
ic(calculateNumberOfSwaps(listaDeStrings))