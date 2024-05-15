def calculeFrequencia(lista):
    freq = {}
    for item in lista:
        freq[item] = 0
    for item in lista:
        freq[item] += 1
    return freq



lista = [2,3,4,'a',1,2,1,'a','b','a']
freq = calculeFrequencia(lista)
print(freq)