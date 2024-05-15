def combinations(n,k,counter = 1,item = -1,permutacao = [],combinacoes = []):
    #k precisa ser menor ou igual n
    #as combinacoes sao descobertas em ordem crescente para evitar repeticoes
    #counter revela a chamada da funcao
    if len(permutacao) == k:
        combinacoes.append(permutacao)
        #permutacao = permutacao[:-1]
        return counter,permutacao,combinacoes
    itemAntigo = item
    for i in range(itemAntigo+1,n-k+counter-1+1):
        item = i
        permutacao.append(item)
        counter += 1
        counter,permutacao,combinacoes = combinations(n,k,counter,item,permutacao,combinacoes)
        counter -= 1
        permutacao = permutacao[:-1]
    return counter,permutacao,combinacoes

        
counter, permutacao,combinacoes = combinations(n = 5,k = 4,counter = 1,item = -1,permutacao = [],combinacoes = [])                      

print(combinacoes)



def combinationsOfList(lista,k):
    counter, permutacao,combinacoes = combinations(n = len(lista),k = k,counter = 1,item = -1,permutacao = [],combinacoes = [])
    listaDeCombinacoes = []
    for combinacao in combinacoes:
        L=[]
        for item in combinacao:
            L.append(lista[item])
        listaDeCombinacoes.append(L)
    return listaDeCombinacoes


lista = ['banana','pera','maca',1,'casa']

listaDeCombinacoes = combinationsOfList(lista,k=3)
print(listaDeCombinacoes)