def arrangements(n,k,listaDeNumeros = None,permutacao = [],arranjos = []):
    #k precisa ser menor ou igual n
    if listaDeNumeros is None:
        listaDeNumeros = []
        for i in range(n):
            listaDeNumeros.append(i)
    if len(permutacao) == k:
        arranjos.append(permutacao)
        #permutacao = permutacao[:-1]
        return listaDeNumeros,permutacao,arranjos
    for i in range(len(listaDeNumeros)):
        item = listaDeNumeros.pop(i)
        permutacao.append(item)
        listaDeNumeros,permutacao,arranjos = arrangements(n,k,listaDeNumeros,permutacao,arranjos)
        permutacao = permutacao[:-1]
        try:
            listaDeNumeros = listaDeNumeros[:i] + [item] + listaDeNumeros[i:]
        except IndexError:
            listaDeNumeros = listaDeNumeros[:i] + [item]
        #lista.append(item)
    return listaDeNumeros,permutacao,arranjos

        
listaDeNumeros, permutacao,arranjos = arrangements(n=5,k=3,listaDeNumeros = None,permutacao = [],arranjos = [])                      

print(arranjos)



def arrangementsOfList(lista,k):
    listaDeNumeros,permutacao,arranjos = arrangements(n=len(lista),k=k,listaDeNumeros = None,permutacao = [],arranjos = [])
    listaDeArranjos = []
    for arranjo in arranjos:
        L = []
        for item in arranjo:
            L.append(lista[item])
        listaDeArranjos.append(L)
    return listaDeArranjos



lista = ['banana','pera','maca',1,'casa']

listaDeArranjos = arrangementsOfList(lista,k=4)

print(listaDeArranjos)