def placaDoClienteCabeNaPlacaDaEmpresa(xEmpresa,yEmpresa,xCliente,yCliente):
    A = [xEmpresa,yEmpresa]
    A.sort()
    xEmpresa,yEmpresa = A
    B = [xCliente,yCliente]
    B.sort()
    xCliente,yCliente = B
    if xCliente<=xEmpresa and yCliente <= yEmpresa:
        print('Sim')
    else:
        print('Nao')


def solveProblem():
    while True:
        try:
            xEmpresa,yEmpresa,M = [int(r) for r in input().split()]
            for _ in range(M):
                xCliente, yCliente = [int(r) for r in input().split()]
                placaDoClienteCabeNaPlacaDaEmpresa(xEmpresa,yEmpresa,xCliente,yCliente)
        except EOFError:
            break

solveProblem()