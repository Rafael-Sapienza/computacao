def decifre(n):
    L=[0,0]
    counter = 0
    for numero in n:
        numero = int(numero)
        L[counter] += numero
        counter = (counter + 1)%2
    string = str(L[0]) + str(L[1])
    soma = 0
    for i in string:
        i = int(i)
        soma += i
    print(soma)

def main():
    N = int(input())
    while N != 0:
        for _ in range(N):
            n = input()
            decifre(n)
        N = int(input())
    
main()

