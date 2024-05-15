def maxDeRepeticoesCaracter(string):
    listaDeCaracteres = ['A','C','G','T']
    freq = {}
    freqTemporaria = {}
    for item in listaDeCaracteres:
        freq[item] = 0
        freqTemporaria[item] = 0
    for i in range(len(string)-1):
        item0 = string[i]
        item1 = string[i+1]
        if item0 == item1:
            freqTemporaria[item0] += 1
        else:
            freqTemporaria[item0] += 1
            if freq[item0] < freqTemporaria[item0]:
                freq[item0] = freqTemporaria[item0]
            freqTemporaria[item0] = 0
    freqTemporaria[string[-1]] += 1
    if freq[string[-1]] < freqTemporaria[string[-1]]:
        freq[string[-1]] = freqTemporaria[string[-1]]
    return freq


def maiorRepeticao(freq):
    maiorNumero = 0
    for value in freq.values():
        if value > maiorNumero:
            maiorNumero = value
    return maiorNumero


string = input()
freq = maxDeRepeticoesCaracter(string)
maiorNumero = maiorRepeticao(freq)
print(maiorNumero)











