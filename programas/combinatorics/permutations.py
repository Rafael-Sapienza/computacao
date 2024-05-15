def permutations(n,listaDeNumeros = None,permutacao = [],permutacoes = []):
    if listaDeNumeros is None:
        listaDeNumeros = []
        for i in range(n):
            listaDeNumeros.append(i)
    if len(permutacao) == n:
        permutacoes.append(permutacao)
        #permutacao = permutacao[:-1]
        return listaDeNumeros,permutacao,permutacoes
    for i in range(len(listaDeNumeros)):
        item = listaDeNumeros.pop(i)
        permutacao.append(item)
        listaDeNumeros,permutacao,permutacoes = permutations(n,listaDeNumeros,permutacao,permutacoes)
        permutacao = permutacao[:-1]
        try:
            listaDeNumeros = listaDeNumeros[:i] + [item] + listaDeNumeros[i:]
        except IndexError:
            listaDeNumeros = listaDeNumeros[:i] + [item]
        #lista.append(item)
    return listaDeNumeros,permutacao,permutacoes

        
listaDeNumeros, permutacao,permutacoes = permutations(n=5,listaDeNumeros = None,permutacao = [],permutacoes = [])                      

print(permutacoes)