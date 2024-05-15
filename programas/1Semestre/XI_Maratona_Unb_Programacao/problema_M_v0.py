from icecream import ic 
import copy
#numeroDeUnidadaes = len(custosSum)= len(custos)
def getInput():
    numeroDeUnidades,dinheiro= [int(r) for r in input().split()]
    ataques = []
    custos = []
    for _ in range(numeroDeUnidades):
        ataques.append([int(r) for r in input().split()])
        custos.append([int(r) for r in input().split()])
    return numeroDeUnidades,dinheiro,ataques,custos

def sumOfCustos(custos):
    def SumOfKthCusto(custos, k):    
        L = [0]
        custo =  copy.deepcopy(custos[k])
        i = 0
        while True:
            if i == 0:
                value = custo[i]
                L.append(value)
            else:
                value += custo[i]
                L.append(value)
            i+=1
            if i >=len(custo):
                return L
                break
    L = []
    for k in range(len(custos)):
        L.append(SumOfKthCusto(custos, k))
    return L

result=0
def findSums(custosSum,dinheiro,numeroDeUnidades,i=0, nestedList = None,A=[]):
    global result
    if i == 0:
        nestedList = []
    if i>=numeroDeUnidades:
        if len(nestedList)==len(custosSum):
            nestedListCopy = copy.deepcopy(nestedList)
            A.append(nestedListCopy)
            result -= custosSum[-1][nestedList[-1]]
            nestedList.pop()
    else:
        result2 = result
        for r in range(len(custosSum[i])):
            result = result2 + custosSum[i][r]
            
            if result> dinheiro:
                if len(nestedList)==len(custosSum):
                    nestedListCopy = copy.deepcopy(nestedList)
                    A.append(nestedListCopy)
                    result -= custosSum[-1][nestedList[-1]]
                    nestedList.pop()
            else:
                if len(nestedList)>=i+1:
                    nestedList[i] = r
                    nestedList = nestedList[:i+1]
                    result = 0
                    for k in range(len(nestedList)):
                        result += custosSum[k][nestedList[k]]

                else:
                    nestedList.append(r)#nesse caso, o result já foi acrescentado logo após o for      
                findSums(custosSum,dinheiro, numeroDeUnidades,i=i+1, nestedList=nestedList,A=A)
    return A 

def findIndexesInAtaques(indicesPossiveisPrecosPorUnidade):
    def findIndexInAtaques(indicesPossiveisPrecosPorUnidade,k):
        indice = indicesPossiveisPrecosPorUnidade[k]
        L = []
        for r in indice:
            if r == 0:
                L.append([])
            else:
                L.append(r-1)
        return L    
    
    indexes = []
    for k in range(len(indicesPossiveisPrecosPorUnidade)):
        indexes.append(findIndexInAtaques(indicesPossiveisPrecosPorUnidade,k))
    return indexes
        
def findMaxAtaque(indexesAtaques, ataques):
    def findAtaqueValue(indexesAtaques, ataques, k):
        index = indexesAtaques[k]
        ataqueValue = 0
        for i in range(len(index)):
            r = index[i]
            if r or r==0:
                ataqueValue += ataques[i][r]
        return ataqueValue    
    
    valoresPossiveisDeAtaques = []
    for k in range(len(indexesAtaques)):
        ataqueValue = findAtaqueValue(indexesAtaques, ataques, k)
        valoresPossiveisDeAtaques.append(ataqueValue)
    valoresPossiveisDeAtaquesCopy = copy.deepcopy(valoresPossiveisDeAtaques)
    valoresPossiveisDeAtaquesCopy.sort()
    maxAtaque = valoresPossiveisDeAtaquesCopy[-1]
    index = valoresPossiveisDeAtaques.index(maxAtaque)
    bestIndexInAtaques = indexesAtaques[index]
    return maxAtaque, bestIndexInAtaques 

def printResult(maxAtaque,bestIndexInAtaques):
    numeroDeUnidadesContratadas = 0
    for r in bestIndexInAtaques:
        if r or r==0:
            numeroDeUnidadesContratadas += 1
    if numeroDeUnidadesContratadas==0:
        print(maxAtaque,numeroDeUnidadesContratadas)
    else:
        print(maxAtaque,numeroDeUnidadesContratadas)
        for k in range(len(bestIndexInAtaques)):
            if bestIndexInAtaques[k] or bestIndexInAtaques[k]==0:
                print(k+1,bestIndexInAtaques[k])


'''
ataques = [[1,2,4,8],[1,2,3,10],[2,3,4,5],[5,8,12,15],[20,30,50,100]] 
numeroDeUnidades = 5
custos = [[10,20,30,40],[10,20,30,40],[5,10,15,20],[30,50,80,90],[50,80,120,150]]
dinheiro = 100
'''

'''
ataques = [[1,3,5,9],[5,9,12,15],[5,10,15,20] ] 
numeroDeUnidades = 3
custos = [[1,4,7,10],[4,10,15,20],[6,12,18,24]]
dinheiro = 10
'''

numeroDeUnidades,dinheiro,ataques,custos = getInput()
#ic(numeroDeUnidades,dinheiro,ataques,custos)

custosSum = sumOfCustos(custos)
#ic(custosSum)

indicesPossiveisPrecosPorUnidade = findSums(custosSum,dinheiro, numeroDeUnidades)
#SAO OS INDICES DE custosSum
#ic(indicesPossiveisPrecosPorUnidade)

indexesAtaques = findIndexesInAtaques(indicesPossiveisPrecosPorUnidade)
#ic(indexesAtaques)

maxAtaque, bestIndexInAtaques = findMaxAtaque(indexesAtaques, ataques)
#ic(maxAtaque,bestIndexInAtaques)

printResult(maxAtaque,bestIndexInAtaques)