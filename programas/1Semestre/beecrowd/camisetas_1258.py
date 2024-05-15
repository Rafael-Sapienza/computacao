def ordenacao(n):
    myDict = {'branco':{
        'P':[],
        'M':[],
        'G':[],
    },
              'vermelho':{
        'P':[],
        'M':[],
        'G':[],
    },          
              }
    
    
    for i in range(n):
        nome = input()
        cor, tamanho = input().split()
        myDict[cor][tamanho] .append(nome)


    lista1 = ['branco','vermelho']
    lista2 = ['P','M','G']
    for item1 in lista1:
        for item2 in lista2:
            myDict[item1][item2].sort()

    for item1 in lista1:
        for item2 in lista2:
            if myDict[item1][item2]:
                for item in myDict[item1][item2]:
                    s = item1 + ' ' + item2 + ' ' + item
                    print(s)
        


def main():
    n = int(input())
    ordenacao(n)
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            print()
            ordenacao(n)

main()