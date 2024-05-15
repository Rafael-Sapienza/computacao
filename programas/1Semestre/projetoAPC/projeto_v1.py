from icecream import ic


def ondeEstaoAsAspas(stringOriginal):
    posicaoAspasSemPar = []
    posicaoAspasComPar = []
    for i,item in enumerate(stringOriginal):
        if item == '"':
            posicaoAspasSemPar.append(i)
            if len(posicaoAspasSemPar) == 2:
                posicaoAspasComPar.append(posicaoAspasSemPar)
                posicaoAspasSemPar = []
    return posicaoAspasComPar,posicaoAspasSemPar

            
def anuleEspacosEntreAspas(stringOriginal,posicaoAspasComPar):
    s = ''
    if posicaoAspasComPar:
        primeiroValor = 0
        segundoValor = posicaoAspasComPar[0][0]
        s += stringOriginal[primeiroValor:segundoValor]
        for i in range(len(posicaoAspasComPar)-1):
            item1 = posicaoAspasComPar[i]
            item2 = posicaoAspasComPar[i+1]
            primeiroValor = item1[1] + 1
            segundoValor = item2[0]
            s += stringOriginal[primeiroValor:segundoValor]
        s += stringOriginal[posicaoAspasComPar[-1][1]+1:]
    else:
        s = stringOriginal
    return s


def erroDaMinusculaEMaiuscula(s):
    erroDaMaiuscula = []
    erroDaMinuscula = []
    for i,item in enumerate(s):
        if item != ' ':
            primeiroCaractere = item
            posicaoDoPrimeiroCaractere = i
            break
    if primeiroCaractere.islower():
        erroDaMinuscula.append(posicaoDoPrimeiroCaractere)
    if primeiroCaractere == '.':
        flag = True
    else:
        flag = False
    for i,item in enumerate(s[posicaoDoPrimeiroCaractere + 1:],start = posicaoDoPrimeiroCaractere + 1): #o primeiro caractere devera ser maiusculo. logo, nao devemos considera-lo no erro de maiuscula, mas sim de minuscula
        if item != ' ':
            if item.islower():
                if flag:
                    erroDaMinuscula.append(i)
            elif item.isupper():
                if not(flag):
                    erroDaMaiuscula.append(i)
            if item == '.':
                flag = True
            elif item != '.':
                flag = False
    return erroDaMaiuscula,erroDaMinuscula


def erroDoEspacoEmBranco(s):
    espacosEmBrancoConsecutivos = []
    flag = False
    for i in range(len(s)-1):
        primeiro = s[i]
        segundo = s[i+1]
        if primeiro == ' ' and segundo == ' ':
            flag = True
        if primeiro != ' ':
            flag = False
        if flag:
            espacosEmBrancoConsecutivos.append(i)
    if s[-2] == ' ' and s[-1] == ' ':
        espacosEmBrancoConsecutivos.append(len(s)-1)
    return espacosEmBrancoConsecutivos

        
def qualOTipoDeCaracter(item):
    tipoDoCaractere = ord(item)
    if tipoDoCaractere <= 57 and tipoDoCaractere >= 48:
        tipoDoCaractere = 'numero'
    elif tipoDoCaractere<=122 and tipoDoCaractere>=97 or tipoDoCaractere>=65 or tipoDoCaractere<=90:
        tipoDoCaractere = 'letra'
    return tipoDoCaractere

def erroDeInformalidade(s):
    marcasQueSeparamPalavras = [' ', '.', ',', '"']
    informalidades = []
    possiveisInformalidades = []
    flag = 'naoExistemLetrasEntreNumeros'
    counter = 0
    for i, item in enumerate(s):
        if item not in marcasQueSeparamPalavras:
            if counter <= 2:
                counter += 1
        else:
            counter = 0
            if flag == 'existemLetrasEntreNumeros':
                informalidades.extend(possiveisInformalidades) #essa parte pega os numeros no final de uma palavra
            possiveisInformalidades = []
        if counter == 1:
            tipoDeCaracter = qualOTipoDeCaracter(item)
        if counter != 0: #está percorndo uma palavra
            if tipoDeCaracter == 'numero':
                    if qualOTipoDeCaracter(item) == tipoDeCaracter:
                        possiveisInformalidades.append(i)
                    else:
                        informalidades.extend(possiveisInformalidades)
                        possiveisInformalidades = []
                        flag = 'existemLetrasEntreNumeros'
            if tipoDeCaracter == 'letra':
                if qualOTipoDeCaracter(item) != tipoDeCaracter:
                    informalidades.append(i)
    return informalidades



def erroDePontuacao(s):
    L = []
    pontuacoes = ['.',',','"']
    for i in range(1,len(s)-1):
        item = s[i]
        if item in pontuacoes:
            if s[i-1] == ' ' and s[i+1]== ' ' or s[i-1] != ' ' and s[i+1] != ' ':
                L.append(i)
    return L


def recupereOIndice(indice,posicaoAspasComPar):
    for item in posicaoAspasComPar:
        if indice>=item[0]:
            indice += item[1] - item[0] + 1
    return indice

def recupereOsIndexesDeLista(listaDeIndexes,posicaoAspasComPar):
    for i,indice in enumerate(listaDeIndexes):
        listaDeIndexes[i] = recupereOIndice(indice,posicaoAspasComPar)
    return listaDeIndexes

def recupereOsIndexesDeDicionario(dicionario,posicaoAspasComPar):
    for key,value in dicionario.items():
        dicionario[key] = recupereOsIndexesDeLista(value,posicaoAspasComPar)
    return dicionario


stringOriginal = 'a09.s2"sgahjgkafsklhfj"  d"gkjlkgsdj"kgflgklgj"3 '


posicaoAspasComPar,posicaoAspasSemPar = ondeEstaoAsAspas(stringOriginal)
ic(posicaoAspasComPar,posicaoAspasSemPar)

s = anuleEspacosEntreAspas(stringOriginal,posicaoAspasComPar)
ic(s)


erros = {}
erros['MAIUSCULA'],erros['MINUSCULA'] = erroDaMinusculaEMaiuscula(s)

erros['ESPACO EM BRANCO'] = erroDoEspacoEmBranco(s)

erros['INFORMAL'] = erroDeInformalidade(s)

erros['PONTUACAO'] = erroDePontuacao(s)

erros = recupereOsIndexesDeDicionario(erros,posicaoAspasComPar)


ic(erros)

#nao esqueca de recuperar os indices iniciais !!!
'''
'''