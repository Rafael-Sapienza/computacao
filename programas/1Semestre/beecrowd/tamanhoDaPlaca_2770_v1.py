def minimoEntreDoisNumeros(a,b):
    if a<=b:
        return a,b
    else:
        return b,a

def placaDoClienteCabeNaPlacaDaEmpresa(xEmpresa,yEmpresa,xCliente,yCliente):
    if xCliente*yCliente>xEmpresa*yEmpresa:
        print('Nao')
    elif not(xCliente<=xEmpresa and yCliente <= yEmpresa):
        print('Nao')
    else:
        print('Sim')

def solveProblem():
    while True:
        try:
            xEmpresa,yEmpresa,M = [int(r) for r in input().split()]
            xEmpresa, yEmpresa = minimoEntreDoisNumeros(xEmpresa,yEmpresa)
            for _ in range(M):
                xCliente, yCliente = [int(r) for r in input().split()]
                xCliente,yCliente = minimoEntreDoisNumeros(xCliente,yCliente)
                placaDoClienteCabeNaPlacaDaEmpresa(xEmpresa,yEmpresa,xCliente,yCliente)
        except EOFError:
            break

solveProblem()