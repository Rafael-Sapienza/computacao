def fib(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    L = [0,1]
    counter = 2
    while counter <= k:
        proximo = L[0] + L[1]
        L = [L[1],proximo]
        counter += 1
    return proximo

    
def main(n):
    for _ in range(n):
        k = int(input())
        x = fib(k)
        print(f'Fib({k}) = {x}')

n = int(input())
main(n)