def quantosMeteoros():
    counter = 1
    while True:
            A = [int(r) for r in input().split()]
            if A ==[0,0,0,0]:
                break
            print(f'Teste {counter}')
            counter += 1
            x1,y1,x2,y2 = A
            meteorosQueCairamNaFazenda = 0
            numeroDeMeteoros = int(input())
            for _ in range(numeroDeMeteoros):
                 x , y = [int(r) for r in input().split()]
                 if x>=x1 and x<= x2:
                      if y>=y2 and y<=y1:
                           meteorosQueCairamNaFazenda += 1
            print(meteorosQueCairamNaFazenda)
                           

quantosMeteoros()