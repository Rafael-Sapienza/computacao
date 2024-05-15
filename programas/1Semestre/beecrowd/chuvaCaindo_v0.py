from icecream import ic

def findVazao(l,k,t1,t2,h):
    vazao1 = h/t1
    a=t1
    b = -k*t2-k*t1-h
    c = k*l

    delta = b**2-4*a*c
    
    if delta >= 0:
        vazao2 = (-b-(delta)**(0.5))/(2*a)
        vazao3 = (-b+(delta)**(0.5))/(2*a)
    else:
        vazao2 = 0
        vazao3 = 0
    
    a = 2*t1
    b = -h-2*k*t1-k*t2-l
    c=2*k*l

    delta = b**2 - 4*a*c

    if delta >= 0:
        vazao4 = (-b-(delta)**(0.5))/(2*a)
        vazao5 = (-b+(delta)**(0.5))/(2*a)
    else:
        vazao4 = 0
        vazao5 = 0
    return vazao1, vazao2, vazao3, vazao4, vazao5

def findPrecipitacoes(l,h,vazao2, vazao3, vazao4, vazao5):
    precipitacoes = []
    if h<=l:
        precipitacoes.append(h)
    if vazao2!=0:
        #if t1>l/vazao2 and t2<=(vazao2*t1 - k*(t1-l/vazao2) - l)/k:
        if t1>l/vazao2 and h>=l:
            precipitacoes.append(vazao2*t1)

    if vazao3 != 0:
        #if t1>l/vazao3 and t2<=(vazao3*t1 - k*(t1-l/vazao3) - l)/k:
        if t1>l/vazao3 and h>=l:
            precipitacoes.append(vazao3*t1)

    if vazao4 != 0:
        #if t1>l/vazao4 and t2>(vazao4*t1 - k*(t1-l/vazao4) - l)/k:
        if t1>l/vazao4 and h==l:
            precipitacoes.append(vazao4*t1)
    
    if vazao5 != 0:
        #if t1>l/vazao5 and t2>(vazao5*t1 - k*(t1-(l/vazao5)) - l)/k:
        if t1>l/vazao5 and h==l:
            precipitacoes.append(vazao5*t1)

    return precipitacoes


#A recurssão está nessa funcao:
def sortList(A, L=[]):
    def minimumNumberOfList(A):
        minimum = A[0]
        minimumIndex = 0
        for index,item in enumerate(A[1:],1):
            if item < minimum:
                minimum = item
                minimumIndex = index
        return minimumIndex, minimum
    
    if len(A)>0:    
        index, minimum = minimumNumberOfList(A)
        L += [minimum]
        A.pop(index)
        L = sortList(A,L)
    else:
        pass
    return L


l,k,t1,t2,h = [float(r) for r in input().split()]
vazao1, vazao2, vazao3, vazao4, vazao5 = findVazao(l,k,t1,t2,h)
precipitacoes = findPrecipitacoes(l,h,vazao2, vazao3, vazao4, vazao5)
#precipitacoes = removeEmptyLists(precipitacoes)
precipitacoes = sortList(precipitacoes)
menorPrecipitacao = precipitacoes[0]
maiorPrecipitacao = precipitacoes[-1]

print(f'{menorPrecipitacao:.9f} {maiorPrecipitacao:.9f}')
        










