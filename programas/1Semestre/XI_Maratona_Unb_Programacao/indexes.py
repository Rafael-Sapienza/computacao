

def swapIndexesToRemove(r,indexesToRemove,k):
    #r é uma lista de indices
    indexesToRemove = indexesToRemove[1:]
    indexesToRemove = [indexesToRemove[k]]
    
    i=0
    if len(r) == 1:
        #i=0
        for s in indexesToRemove:
            if s[0] < r[0]:
                pass
            elif s[0] == r[0]:
                indexesToRemove.remove(s)
            else:
                indexesToRemove[i][0] -= 1 
            #i+=1
    else: 
        #i=0
        for s in indexesToRemove:
            if r[:len(r)-1] == s[:len(r)-1]:
                if s[len(r)-1] < r[-1]:
                    pass
                elif s[len(r)-1] == r[-1]:
                    indexesToRemove.remove(s)
                else:
                    indexesToRemove[i][len(r)-1] -= 1 
            #i+=1

    return indexesToRemove





def finalIndexes(r,indexesToRemove):
    x = len(indexesToRemove)
    A=[]
    for k in range(x-1):
        A.extend(swapIndexesToRemove(r,indexesToRemove,k))
    return A





print( swapIndexesToRemove(r=[9,10],indexesToRemove=[[0],[2,4],[7,8],[9,12,11]],k=2))
print(finalIndexes(r = [0],indexesToRemove = [[0],[1,1],[2]]))