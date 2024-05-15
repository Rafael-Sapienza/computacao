def solveProblem(N):
    for _ in range(N):
        numeroDeStrings = int(input())
        total = 0
        for i in range(numeroDeStrings):
            s = input()
            total += i*len(s)
            total += (len(s) - 1)*len(s)//2
            for element in s:
                codigoAsc2 = ord(element)
                codigoAsc2 -= 65
                total += codigoAsc2
        print(total)


N = int(input())
solveProblem(N)