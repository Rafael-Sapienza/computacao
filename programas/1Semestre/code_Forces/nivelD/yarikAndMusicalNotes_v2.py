import math

def howManyPairsOfNotesHaveSameCombination(n,A):
    #A eh a lista com as notas a1,..,an
    #n eh len(A)
    #arraySemRepeticao serah uma lista formada por A, anulando-se as repeticoes
    #numeroDeReticoes serah uma lista contendo o numero de vezes que cada elemento de arraySemRepeticao se repete em A
    A.sort()
    arraySemRepeticao = []
    numeroDeRepeticoes = []
    counterRepeticoes = 1
    for i in range(n-1):
        item1 = A[i]
        item2 = A[i+1]
        if item1 == item2:
            counterRepeticoes += 1
        else:
            arraySemRepeticao.append(item1)
            numeroDeRepeticoes.append(counterRepeticoes)
            counterRepeticoes = 1
        if i == n-2:
            arraySemRepeticao.append(A[-1])
            numeroDeRepeticoes.append(counterRepeticoes)
            del counterRepeticoes

    counter = 0
    for item in numeroDeRepeticoes:
        #counter += math.comb(item,2) --> vamos deixar mais eficiente
        counter += item*(item-1)//2
    m = len(arraySemRepeticao)
    for i in range(m-1):
        elemento1 = arraySemRepeticao[i]
        '''for j in range(i+1,m):
            if arraySemRepeticao[j] + math.log(arraySemRepeticao[i],2) == arraySemRepeticao[i] + math.log(arraySemRepeticao[j],2):
                counter += 1*numeroDeRepeticoes[i]*numeroDeRepeticoes[j]'''
        #elemento2/elemento1 tem que resultar em uma potencia de 2, ie, elemento2/elemento1 = 2**(algum inteiro)
        for k in range(1,int(math.log((arraySemRepeticao[-1]/elemento1),2))+1):
            #garante que elemento1*(2**k) <= arraySemRepeticao[-1]
            elemento2 = elemento1*(2**k)
            if elemento2 + math.log(elemento1,2) == elemento1 + math.log(elemento2,2):
                try:
                    indiceDoElemento2EmArraySemRepeticao = arraySemRepeticao.index(elemento2)
                    counter += numeroDeRepeticoes[i]*numeroDeRepeticoes[indiceDoElemento2EmArraySemRepeticao]
                except ValueError:
                    pass
    return counter


def solveProblemForAllTestCases(numberOfTestCases):
    for _ in range(numberOfTestCases):
        lengthOfArray = int(input())
        array = [int(r) for r in input().split()]
        numberOfPairs = howManyPairsOfNotesHaveSameCombination(lengthOfArray,array)
        print(numberOfPairs)




numberOfTestCases = int(input())
solveProblemForAllTestCases(numberOfTestCases)


