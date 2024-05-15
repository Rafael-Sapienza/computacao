A=[r for r in input().split()]

horas=[]


B=[]
for r in A:
    C=[int(i) for i in r.split(':')]
    B.append(C)
    #B.append(r.split(':'))

pA = 60*B[0][0] + B[0][1]

cB = 60*B[1][0] + B[1][1]

pB = 60*B[2][0] + B[2][1]

cA = 60*B[3][0] + B[3][1]










for q in range(-12,12):
    tempo_de_voo = (60*24*q+cB+cA-pA-pB)/2

    if tempo_de_voo%1==0 and tempo_de_voo>0 and tempo_de_voo<24*60:
        
        #print(tempo_de_voo)
        
        break


for q in range(-6,6):
    fuso_horario = (60*24*q - pA + cB - tempo_de_voo)/60

    if fuso_horario%1==0 and fuso_horario<=12 and fuso_horario>-12:
        
        #print(fuso_horario)

        break

tempo_de_voo = int(tempo_de_voo)

fuso_horario = int(fuso_horario)

print(f'{tempo_de_voo} {fuso_horario}')

