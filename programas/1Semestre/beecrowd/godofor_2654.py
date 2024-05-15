def quemSeraOGodofor(n):
    myDict = {}
    poder = {}
    qntdDeDeusesMortos = {}
    quantasVezesMorreu = {}
    for _ in range(n):
        L = [r for r in input().split()]
        for i in range(1,4):
            L[i] = int(L[i])
        myDict[L[0]] = L[1:]
    for key,value in myDict.items():
        individualPower = value[0]
        if individualPower not in poder:
            poder[individualPower] = [key]
        else:
            poder[individualPower].append(key)
    L = sorted(poder,reverse=True)
    deusesMaisPoderosos = poder[L[0]]
    if len(deusesMaisPoderosos) == 1:
        deusVencedor = deusesMaisPoderosos[0]
        return deusVencedor
    for item in deusesMaisPoderosos:
        individualQntdDeDeuseMortos = myDict[item][1]
        if individualQntdDeDeuseMortos not in qntdDeDeusesMortos:
            qntdDeDeusesMortos[individualQntdDeDeuseMortos] = [item]
        else:
            qntdDeDeusesMortos[individualQntdDeDeuseMortos].append(item)
    L = sorted(qntdDeDeusesMortos, reverse = True)
    deusesQueMaisMataram = qntdDeDeusesMortos[L[0]]
    if len(deusesQueMaisMataram) == 1:
        deusVencedor = deusesQueMaisMataram[0]
        return deusVencedor
    for item in deusesQueMaisMataram:
        individualqntdVezesQueMorreu = myDict[item][2]
        if individualqntdVezesQueMorreu not in quantasVezesMorreu:
            quantasVezesMorreu[individualqntdVezesQueMorreu] = [item]
        else:
            quantasVezesMorreu[individualqntdVezesQueMorreu].append(item)
    L = sorted(quantasVezesMorreu)
    deusesQueMenosMorreram = quantasVezesMorreu[L[0]]
    if len(deusesQueMenosMorreram) == 1:
        deusQueMenosMorreu = deusesQueMenosMorreram[0]
        return deusQueMenosMorreu
    else:
        deusesQueMenosMorreram.sort()
        deusVencedor = deusesQueMenosMorreram[0]
        return deusVencedor
    
n = int(input())
deusVencedor = quemSeraOGodofor(n)
print(deusVencedor)

    

        
