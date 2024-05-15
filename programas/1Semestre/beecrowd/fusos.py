
A=[r for r in input().split()]

horas=[]
for r in A:
    B=[]
    B.extend(r.split(':'))
    horas.append(int(B[0]))

pA, cB, pB, cA = horas

'''
if cB >= pA and cA>=pB:
    tempo_de_voo = (cA+cB-pA-pB)/2
    fuso_horario = cB-pA-tempo_de_voo

elif cB < pA and cA>=pB:
    tempo_de_voo = (cA+cB-pA-pB+24)/2
    fuso_horario = tempo_de_voo + pB - cA

elif cB >= pA and cA<pB:
    tempo_de_voo = (cA+cB-pA-pB+24)/2
    fuso_horario = -tempo_de_voo + cB - pA

else:
    tempo_de_voo = (cA+cB-pA-pB + 2*24)/2
    fuso_horario = tempo_de_voo -cA+pB-24

tempo_de_voo = 60*tempo_de_voo

tempo_de_voo = int(tempo_de_voo)
fuso_horario = int(fuso_horario)


print(f'{tempo_de_voo} {fuso_horario}')

###################

for tempo_de_voo in range(0,24):
    for fuso in range(-24,24):
        if (pA+tempo_de_voo+fuso+48)%24 == cB and (pB+tempo_de_voo-fuso+48)%24 == cA:
            if abs(fuso) <= abs(tempo_de_voo):
                tempo_de_voo = 60*tempo_de_voo
                print(f'{tempo_de_voo} {fuso}')
'''

################

for q in range(-12,12):
    tempo_de_voo = (24*q+cB+cA-pA-pB)/2

    if tempo_de_voo%1==0 and tempo_de_voo>0 and tempo_de_voo<24:
        
        break


for q in range(-6,6):
    fuso_horario = 24*q - pA + cB - tempo_de_voo

    if fuso_horario%1==0 and fuso_horario<=12 and fuso_horario>=-12:
        
        break


tempo_de_voo = 60*tempo_de_voo
tempo_de_voo = int(tempo_de_voo)

fuso_horario = int(fuso_horario)

print(f'{tempo_de_voo} {fuso_horario}')

