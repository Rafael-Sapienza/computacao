import math

def somaDeFracoes(a,b,c,d):
    numerador = a*d + c*b
    denominador = b*d
    fatorDeIrreducao = math.gcd(numerador,denominador)
    numerador = numerador//fatorDeIrreducao
    denominador = denominador//fatorDeIrreducao
    print(numerador,denominador)

a,b,c,d = [int(r) for r in input().split()]
somaDeFracoes(a,b,c,d)