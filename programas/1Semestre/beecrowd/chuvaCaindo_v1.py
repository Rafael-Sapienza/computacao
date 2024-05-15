l,k,t1,t2,h = [float(r) for r in input().split()]

def findMaxPrecipitacao(l,k,t1,t2,h, tempo = 0, maxPrecipitacao = 0):
    if h<l:
        maxPrecipitacao = h
    else:
        maxPrecipitacao = h + k*t2
        tempo += 0.01
        maxPrecipitacao += k*0.01
        if t>=t1-l
        findMaxPrecipitacao(l,k,t1,t2,h, tempo = tempo, maxPrecipitacao = maxPrecipitacao)
