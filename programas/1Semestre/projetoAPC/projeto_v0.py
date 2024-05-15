stringOriginal = 'a.   apea. 4alfda. ppp.   Paula.'
s = '4r. O1z "132544354a" a12efda1'
erros = {}






def erroDaMaiuscula(s):
    L = []
    for i in range(len(s)-1):
        primeiro = s[i]
        segundo = s[i+1]
        if segundo.isupper():
            if primeiro != ' ':
                L.append(i+1)
            else:
                for i2 in range(i,-1,-1):
                    item2 = s[i2]
                    if item2 != ' ':
                        if item2 != '.':
                            L.append(i2)
                    break                    
    return L


def erroDaMinuscula(s):
    L = []
    if s[0].islower():
        L.append(0)
    for i,item in enumerate(s):
        if item == '.':
            for i2,item2 in enumerate(s[i+1:],start=i+1) :
                if item2 != ' ':
                    if item2.islower():
                        L.append(i2)
                    break
    return L

def erroDoEspacoEmBranco(s):
    L = []
    flag = False
    for i in range(len(s)-1):
        primeiro = s[i]
        segundo = s[i+1]
        if primeiro == ' ' and segundo == ' ':
            flag = True
        if primeiro != ' ':
            flag = False
        if flag:
            L.append(i)
    if s[-2] == ' ' and s[-1] == ' ':
        L.append(len(s)-1)
    return L


def erroDePontuacao(s):
    L = []
    pontuacoes = ['.',',','"']
    for i in range(1,len(s)-1):
        item = s[i]
        if item in pontuacoes:
            if s[i-1] == ' ' and s[i+1]== ' ' or s[i-1] != ' ' and s[i+1] != ' ':
                L.append(i)
    return L

def qualOTipoDeCaracter(item):
    tipoDoCaractere = ord(item)
    if tipoDoCaractere <= 57 and tipoDoCaractere >= 48:
        tipoDoCaractere = 'numero'
    elif tipoDoCaractere<=122 and tipoDoCaractere>=97 or tipoDoCaractere>=65 or tipoDoCaractere<=90:
        tipoDoCaractere = 'letra'
    return tipoDoCaractere

def erroDeInformalidade(s):
    marcasQueSeparamPalavras = [' ', '.', ',', '"']
    L = []
    flag = False
    counter = 0
    for i in range(len(s)):
        item = s[i]
        if item not in marcasQueSeparamPalavras:
            flag = True
            counter += 1
        if counter == 1:
            tipoDoCaractere = qualOTipoDeCaracter(item)
        elif item in marcasQueSeparamPalavras:
            flag = False
            counter = 0
        elif flag:
            if qualOTipoDeCaracter(item) != tipoDoCaractere:
                L.append(i)
    return L








erros = {}
erros['MAIUSCULA'] = erroDaMaiuscula(s)
erros['MINUSCULA'] = erroDaMinuscula(s)
erros['ESPACO EM BRANCO'] = erroDoEspacoEmBranco(s)
erros['PONTUACAO'] = erroDePontuacao(s)
erros['INFORMAL'] = erroDeInformalidade(s)

print(erros)

