def oQueFalta(dieta,cafe,almoco):
    jantar = ''
    refeicoes = cafe + almoco
    for comida in refeicoes:
        posicao = dieta.find(comida)
        if posicao == -1:
            return('CHEATER')
        dieta = dieta[:posicao] + dieta[posicao + 1:]
    jantar += dieta
    return jantar

def main(n):
    for _ in range(n):
        dieta = input()
        cafe = input()
        almoco = input()
        jantar = oQueFalta(dieta,cafe,almoco)
        if jantar != 'CHEATER':
            L = [r for r in jantar]
            L.sort()
            jantar = ''
            for item in L:
                jantar += item
        print(jantar)


n = int(input())
main(n)
        