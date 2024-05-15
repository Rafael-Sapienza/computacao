def decifre(string):
    L = string.split()
    mensagemOculta = ''
    for item in L:
        mensagemOculta += item[0]
    print(mensagemOculta)

def main(n):
    for _ in range(n):
        string = input()
        decifre(string)

n = int(input())
main(n)