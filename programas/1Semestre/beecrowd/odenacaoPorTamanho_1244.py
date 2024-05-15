def printStringInRightOrder(s):
    myDict = {}
    L = s.split()
    for item in L:
        comprimento = len(item)
        if comprimento in myDict.keys():
            myDict[comprimento].append(item)
        else:
            myDict[comprimento] = [item]
    ordenacao = sorted(myDict, reverse=True)
    a = ''
    for i in ordenacao:
        for objeto in myDict[i]:
            a += objeto + ' '
    a = a[:-1]
    print(a)
         


def main(n):
    for _ in range(n):
        s = input()
        printStringInRightOrder(s)


n = int(input())
main(n)
















