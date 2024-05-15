def qualOValor(A,B,C,D):
    if C%A != 0 or B == A:
        return -1
    i = C
    while True:
        if i < 1:
            return -1
            break
        coeficiente = C/i
        if coeficiente%1 == 0:
            n = coeficiente*A
            n = int(n)
            if n%B != 0 and C%n == 0 and D%n != 0:
                return n
                break
        
        i -= 1

A,B,C,D = [int(r) for r in input().split()]
result = qualOValor(A,B,C,D)
print(result)