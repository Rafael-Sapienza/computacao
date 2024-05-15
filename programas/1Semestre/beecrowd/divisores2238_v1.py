def qualOValor(A,B,C,D):
    if C%A != 0 or B == A:
        return -1
    
    valorNovo1 = -1
    valorNovo2 = -1
    counter = 1
    counter1 = 1
    counter2 = 1
    while True:
        if counter >= int(C**0.5)+1:
            A = [valorNovo1,valorNovo2]
            A.sort()
            if A[0] != -1:
                return A[0]
            else:
                return A[1]
            break
        

        i = counter
        coeficiente = C/i
        if coeficiente%1 == 0:
            n = coeficiente*A
            n = int(n)
            if n%B != 0 and C%n == 0 and D%n != 0:
                possivelValorNovo1 = n
                if counter1 == 1:
                    valorNovo1 = possivelValorNovo1
                    counter1 += 1 
                if possivelValorNovo1<valorNovo1:
                    valorNovo1 = possivelValorNovo1

        i = C//counter
        coeficiente = C/i
        if coeficiente%1 == 0:
            n = coeficiente*A
            n = int(n)
            if n%B != 0 and C%n == 0 and D%n != 0:
                possivelValorNovo2 = n
                if counter2 == 1:
                    valorNovo2 = possivelValorNovo2
                    counter2 += 1
                if possivelValorNovo2<valorNovo2:
                    valorNovo2 = possivelValorNovo2
 

        
        counter += 1

A,B,C,D = [int(r) for r in input().split()]
result = qualOValor(A,B,C,D)
print(result)