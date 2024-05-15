def fibonacci(a,b):
    result = a+b
    return result

def inteirosEntre(c,d):
    L=[]
    if d-c == 0:
        pass
    else:
        for i in range(1,d-c):
            L.append(c+i)
    return L



def fibonot(final, numeroDeTermos = 0,comeco1 = 1, comeco2 = 1):
    proximoFibonacci = fibonacci(comeco1,comeco2)
    elementosDeFibonot = inteirosEntre(comeco2,proximoFibonacci)
    numeroDeTermos2 = numeroDeTermos + len(elementosDeFibonot)
    if numeroDeTermos2 >= final:
        result = elementosDeFibonot[final - numeroDeTermos - 1]
    else:
        result = fibonot(final = final, numeroDeTermos = numeroDeTermos2,comeco1 = comeco2, comeco2 = proximoFibonacci)
    return result


final = int(input())
result = fibonot(final)
print(result)

