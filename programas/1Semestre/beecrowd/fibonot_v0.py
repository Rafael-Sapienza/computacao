def fibonacci(a,b):
    result = a+b
    return result

def inteirosEntre(c,d,L=[]):
    if c+1 < d:
        L += [c+1]
        L = inteirosEntre(c+1,d)
    else:
        pass
    return L



def fibonot(final, numeroDeTermos = 0,comeco1 = 1, comeco2 = 1):
    proximoFibonacci = fibonacci(comeco1,comeco2)
    elementosDeFibonot = inteirosEntre(comeco2,proximoFibonacci,L=[])
    numeroDeTermos2 = numeroDeTermos + len(elementosDeFibonot)
    if numeroDeTermos2 >= final:
        result = elementosDeFibonot[final - numeroDeTermos - 1]
    else:
        result = fibonot(final = final, numeroDeTermos = numeroDeTermos2,comeco1 = comeco2, comeco2 = proximoFibonacci)
    return result



print(fibonot(3))