def listaDePrecos(M):
    precos = {}
    for _ in range(M):
        key,value = input().split()
        value = float(value)
        precos[key] = value
    return precos

def listaDeQuantidades(P):
    quantidades = {}
    for _ in range(P):
        key,value = input().split()
        value = int(value)
        quantidades[key] = value
    return quantidades

def quantoCusta(precos,quantidades):
    counter = 0
    for key in quantidades:
        valor = quantidades[key]*precos[key]
        counter += valor
    return counter

def main():
    N = int(input())
    for _ in range(N):
        M = int(input())
        precos = listaDePrecos(M)
        P = int(input())
        quantidades = listaDeQuantidades(P)
        valorFinal = quantoCusta(precos,quantidades)
        print(f'R$ {valorFinal:.2f}')
main()