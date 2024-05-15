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


def getInput():
    a= int(input())
    b = int(input())
    A=[a,b]
    A = sortList(A)
    x,y = A
    if x%2 == 1:
        x+=2
    else:
        x+=1
    if y%2 == 1:
        y-=2
    else:
        y-=1
    if x>y:
        return 0
    elif x<0 and y>0:
        if abs(x) == abs(y):
            return 0
        elif abs(x) < abs(y):
            x = -(x-2)
        elif abs(x) > abs(y):
            y = -(y+2)
    if x==y:
        return x
    else:
        return x,y


def SomaDeUmAoOutro(result):
    if isinstance(result,int):
        return result
    else:
        x, y = result
        n = (y - x)/2 + 1
        soma = int((x+y)*n/2)
        return soma
        
result = getInput()
soma = SomaDeUmAoOutro(result)
print(soma)