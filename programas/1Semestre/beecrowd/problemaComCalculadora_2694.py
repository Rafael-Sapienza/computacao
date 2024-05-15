def somaPorLinha(s):
    s = s + ' '
    numero = ''
    L = []
    for i, item in enumerate(s):
        asc = ord(item)
        if asc >= 48 and asc <= 57:
            flag = True
        else:
            flag = False
        if flag:
            numero += item
        if not(flag):
            if numero != '':
                L.append(numero)
            numero = ''
    total = 0
    for item in L:
        item = int(item)
        total+=item
    print(total)

def solveProblem():
    N = int(input)
    for i in range(N):
        s = input()
        somaPorLinha(s)