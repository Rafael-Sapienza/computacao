def ondeEstaoAsAspas(stringOriginal):
    simboloDePontuacao = ['.',',']
    posicaoAspasSemPar = []
    posicaoAspasComPar = []
    errosDePontuacaoAdicionais = []
    for i,item in enumerate(stringOriginal):
        if item == '"':
            posicaoAspasSemPar.append(i)
            if i >= 1:
                if stringOriginal[i-1] != ' ' and len(posicaoAspasSemPar) == 1:
                    errosDePontuacaoAdicionais.append(i)
                    
            
            if len(posicaoAspasSemPar) == 2:
                posicaoAspasComPar.append(posicaoAspasSemPar)
                if i >= 1:
                    if stringOriginal[i-1] in simboloDePontuacao:
                        errosDePontuacaoAdicionais.append(i)
                posicaoAspasSemPar = []
    return posicaoAspasComPar,posicaoAspasSemPar,errosDePontuacaoAdicionais

            
def anuleEspacosEntreAspas(stringOriginal,posicaoAspasComPar): #transforma o que estava entre aspas duplas em uma única aspa dupla
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


def erroDaMinusculaEMaiuscula(s):
    erroDaMaiuscula = []
    erroDaMinuscula = []
    for i in range(len(s)-1):
        item = s[i]
        if item != ' ' and item != '"':
            primeiroCaractere = item
            posicaoDoPrimeiroCaractere = i
            break
    if primeiroCaractere.islower():
        erroDaMinuscula.append(posicaoDoPrimeiroCaractere)
    if primeiroCaractere == '.' and s[posicaoDoPrimeiroCaractere+1] == ' ':
        flag = True
    else:
        flag = False
    for i,item in enumerate(s[posicaoDoPrimeiroCaractere + 1:-1],start = posicaoDoPrimeiroCaractere + 1): #o primeiro caractere devera ser maiusculo. logo, nao devemos considera-lo no erro de maiuscula, mas sim de minuscula
        if item != ' ' and item != '"':
            if item.islower():
                if flag:
                    erroDaMinuscula.append(i)
            elif item.isupper():
                if not(flag):
                    erroDaMaiuscula.append(i)
            if item == '.' and (s[i+1] == ' ' or s[i+1] == '"'):
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
        if segundo != ' ':
            flag = False
        if flag:
            espacosEmBrancoConsecutivos.append(i+1)
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
    pontuacoes = ['.',',']
    for i in range(1,len(s)-1):
        item = s[i]
        if item in pontuacoes:
            if s[i-1] == ' ' or (s[i-1] != ' ' and s[i+1] != ' '):
                L.append(i)
    return L


def recupereOIndice(indice,posicaoAspasComPar):
    for item in posicaoAspasComPar:
        if indice>=item[0]:
            indice += item[1] - item[0]
    return indice

def recupereOsIndexesDeLista(listaDeIndexes,posicaoAspasComPar):
    for i,indice in enumerate(listaDeIndexes):
        listaDeIndexes[i] = recupereOIndice(indice,posicaoAspasComPar)
    return listaDeIndexes

def recupereOsIndexesDeDicionario(dicionario,posicaoAspasComPar):
    for key,value in dicionario.items():
        dicionario[key] = recupereOsIndexesDeLista(value,posicaoAspasComPar)
    return dicionario


def printFinalResult(erros):
    if erros['ESPACO EM BRANCO'] == erros['INFORMAL'] == erros['MAIUSCULA'] == erros['MINUSCULA'] == erros['PONTUACAO']:
        print('SIM')
    else:
        print('NAO')
        for key,value in erros.items():
            if value:
                print(f'{key}')
                print(*value)


stringOriginal = input()
#stringOriginal = input()

posicaoAspasComPar,posicaoAspasSemPar,errosDePontuacaoAdicionais = ondeEstaoAsAspas(stringOriginal)

s = anuleEspacosEntreAspas(stringOriginal,posicaoAspasComPar)


erros = {}
erros['ESPACO EM BRANCO'] = erroDoEspacoEmBranco(s)

erros['INFORMAL'] = erroDeInformalidade(s)

erros['MAIUSCULA'],erros['MINUSCULA'] = erroDaMinusculaEMaiuscula(s)

erros['PONTUACAO'] = erroDePontuacao(s)

erros = recupereOsIndexesDeDicionario(erros,posicaoAspasComPar)


if errosDePontuacaoAdicionais and posicaoAspasSemPar:
    if errosDePontuacaoAdicionais[-1] == posicaoAspasSemPar[0]:
        erros['PONTUACAO'] += errosDePontuacaoAdicionais
else:
    erros['PONTUACAO'] += errosDePontuacaoAdicionais + posicaoAspasSemPar

erros['PONTUACAO'].sort()


printFinalResult(erros)

#nao esqueca de recuperar os indices iniciais !!!
'''
'''