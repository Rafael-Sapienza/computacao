def lowerCase(char):
    if char.isupper():
        x = ord(char)
        x += 32
        char = chr(x)
        return char
    else:
        return char

def makeDict(string):
    freq = {}
    for item in string:
        if item.isalpha():
            item = lowerCase(item)
            if item not in freq:
                freq[item] = 1
            else:
                freq[item] += 1
    return freq

def invDict(freq):
    dictInv = {}
    for key,value in freq.items():
        if value not in dictInv:
            dictInv[value] = [key]
        else:
            dictInv[value].append(key)
    return dictInv

def printBasedOnFrequencies(dictInv):
    L = sorted(dictInv, reverse = True)
    mariorFrequencia = L[0]
    letrasQueMaisAparecem = dictInv[mariorFrequencia]
    letrasQueMaisAparecem.sort()
    print(*letrasQueMaisAparecem,sep = '')


def main():
    n = int(input())
    for _ in range(n):
        string = input()
        freq = makeDict(string)
        dictInv = invDict(freq)
        printBasedOnFrequencies(dictInv)

main()
