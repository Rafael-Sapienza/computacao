from icecream import ic

#Funcoes uteis:

def nested_list(A, depth=None, length=None):
    if depth is None:
        depth = len(A)
    if length is None:
        length = A[-1]

    if depth == 1:
        return [0] * A[0]
    else:
        my_list = []
        return [nested_list(A, depth=depth-1, length=A[-depth]) for _ in range(length)]

#Inputs:

def getInput():
    listaInput = [int(r) for r in input().split()]
    numeroDeBumpers = listaInput[0]
    posicaoInicial = listaInput[1]
    energiaInicial = listaInput[2]
    bumpersEnergy = nested_list([0,numeroDeBumpers])
    bumpersEnergy[posicaoInicial-1] = [energiaInicial]
    return [numeroDeBumpers, bumpersEnergy]

#Resolver problema:

def nextEnergy(numeroDeBumpers,bumpersEnergy):
    newEnergy = nested_list([0,numeroDeBumpers])
    for i in range(numeroDeBumpers):#iterar lista bumpersEnergy
        if i == 0:
            for r in bumpersEnergy[i]:
                if r > 0:
                    newEnergy[i+1].append(r-1)
        elif i == numeroDeBumpers - 1:
            for r in bumpersEnergy[i]:
                if r > 0:
                    newEnergy[i-1].append(r-1)
        else:
            for r in bumpersEnergy[i]:
                if r>0:
                    newEnergy[i+1].append(r-1)
                    newEnergy[i-1].append(r-1)
    return newEnergy

def calculateCurrentPunctuaction(numeroDeBumpers,bumpersEnergy):
    currentBumpersPunctuaction = nested_list([0,numeroDeBumpers]) 
    for i in range(numeroDeBumpers):#iterar lista bumpersEnergy
        currentBumpersPunctuaction[i].append(len(bumpersEnergy[i]))
    return currentBumpersPunctuaction

def calculateFinalPunctuaction(numeroDeBumpers,bumpersEnergy):
    if numeroDeBumpers == 1:
        finalResult = [[1]]
        return finalResult
    else:
        finalResult = nested_list([1,numeroDeBumpers])
        while True:
            currentBumpersPunctuaction=calculateCurrentPunctuaction(numeroDeBumpers,bumpersEnergy)
            bumpersEnergy = nextEnergy(numeroDeBumpers,bumpersEnergy)
            for i in range(len(finalResult)):
                finalResult[i][0] += currentBumpersPunctuaction[i][0]
            if bumpersEnergy == nextEnergy(numeroDeBumpers,bumpersEnergy):
                return finalResult
                break

def printFinalResult(lista):
    x=''
    for i in range(len(lista)):
        if i <= len(lista) - 2:
            x = x + str(lista[i][0])+' '
        else:
            x = x + str(lista[i][0])
    print(x)

#Chamadas das funcoes:

numeroDeBumpers,bumpersEnergy = getInput()
finalResult = calculateFinalPunctuaction(numeroDeBumpers,bumpersEnergy)
ic(finalResult)
printFinalResult(finalResult)