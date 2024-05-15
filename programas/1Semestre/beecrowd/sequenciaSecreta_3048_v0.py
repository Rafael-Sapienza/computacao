def numerosQuePodemSerMarcados(N, valorAntigo = 0, total = 0):
    for i in range(N):
        valorNovo = int(input())
        if valorNovo != valorAntigo:
            total += 1
        valorAntigo = valorNovo
    print(total)

N = int(input())
numerosQuePodemSerMarcados(N)