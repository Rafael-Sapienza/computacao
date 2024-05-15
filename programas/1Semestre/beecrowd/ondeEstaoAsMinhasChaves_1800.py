def main(escritorios,Q):
    for _ in range(Q):
        x = int(input())
        if x in escritorios:
            print(0)
        else:
            print(1)
            escritorios.append(x)


Q,E = [int(r) for r in input().split()]
escritorios = [int(r) for r in input().split()]
main(escritorios,Q)

