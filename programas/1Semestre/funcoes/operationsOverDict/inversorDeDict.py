def invertaDict(dicionario):
    invDict = {}
    for value in dicionario.values():
        invDict[value] = []
    for key,value in dicionario.items():
        invDict[value].append(key)
    return invDict

dicionario = {'a':2,
              'c':1,
              'd':2}

invDict = invertaDict(dicionario)
print(invDict)