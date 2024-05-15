def makeDict(m):
    traducao = {}
    for _ in range(m):
        key = input()
        value = input()
        traducao[key] = value
    return traducao

def traduza(traducao, n):
    palavrasEmPortugues = []
    for _ in range(n):
        palavrasEmPortugues = []
        palavrasEmJapones = input().split()
        for char in palavrasEmJapones:
            if char in traducao:
                palavraEmPortugues = traducao[char]
                palavrasEmPortugues.append(palavraEmPortugues)
            else:
                palavrasEmPortugues.append(char)
        print(*palavrasEmPortugues)

def main():
    N = int(input())
    for _ in range(N):
        m,n = [int(r) for r in input().split()]
        traducao = makeDict(m)
        traduza(traducao,n)
        print()

main()