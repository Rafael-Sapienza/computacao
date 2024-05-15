A=[r for r in input().split()]

horas=[]
for r in A:
    B=[]
    B.extend(r.split(':'))
    horas.append(int(B[0]))

pA, cB, pB, cA = horas


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
