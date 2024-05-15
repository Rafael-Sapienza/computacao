from icecream import ic



def ondeEstaoAsAspas(stringOriginal):
    simboloDePontuacao = ['.',',']
    posicaoAspasSemPar = []
    posicaoAspasComPar = []
    errosDePontuacao = []
    for i,item in enumerate(stringOriginal):
        if item == '"':
            posicaoAspasSemPar.append(i)
            if i >= 1:
                if stringOriginal[i-1] != ' ':
                    errosDePontuacao.append(i)
            
            if len(posicaoAspasSemPar) == 2:
                posicaoAspasComPar.append(posicaoAspasSemPar)
                if i >= 1:
                    if stringOriginal[i-1] in simboloDePontuacao:
                        errosDePontuacao.append(i)
                posicaoAspasSemPar = []
    return posicaoAspasComPar,posicaoAspasSemPar,errosDePontuacao



def anuleEspacosEntreAspas(stringOriginal,posicaoAspasComPar):
    s = ''
    if posicaoAspasComPar:
        primeiroValor = 0
        segundoValor = posicaoAspasComPar[0][0] 
        s += stringOriginal[primeiroValor:segundoValor] + '"'
        for i in range(len(posicaoAspasComPar)-1):
            item1 = posicaoAspasComPar[i]
            item2 = posicaoAspasComPar[i+1]
            primeiroValor = item1[1] + 1
            segundoValor = item2[0]
            s += stringOriginal[primeiroValor:segundoValor] + '"'
        s += stringOriginal[posicaoAspasComPar[-1][1]+1:]
    else:
        s = stringOriginal
    return s

def recupereOIndice(indice,posicaoAspasComPar):
    for item in posicaoAspasComPar:
        if indice>=item[0]:
            indice += item[1] - item[0]
    return indice

stringOriginal = '"casa fakda"crianca"asdj"bola'

posicaoAspasComPar,posicaoAspasSemPar,errosDePontuacao = ondeEstaoAsAspas(stringOriginal)


ic(posicaoAspasComPar,posicaoAspasSemPar,errosDePontuacao)

