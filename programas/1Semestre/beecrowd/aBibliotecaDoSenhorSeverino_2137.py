def ordeneCadastros(n):
    L = []
    for _ in range(n):
        x = input()
        L.append(x)
    L.sort()
    for item in L:
        print(item)

def main():
    while True:
        try:
            n = int(input())
            ordeneCadastros(n)
        except EOFError:
            break

main()