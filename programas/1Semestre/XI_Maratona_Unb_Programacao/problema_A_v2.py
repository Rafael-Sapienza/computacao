import copy

#inputs:

H = [int(r) for r in input().split()]

N , M, D = H

B=[]
for _ in range(M):
	B.append([int(r) for r in input().split()])

print(B)


C=[]
for i in range(len(B)):
	C.append(B[i][0:2])

print(C)



T=[]
for i in range(len(B)):
	T.append(B[i][2])





#functions:
def find_all_element_in_nested_list(data, element_to_find, index=[]):
    indexes = []
    for i, item in enumerate(data):
        if item == element_to_find:
            indexes.append(index + [i])
        elif isinstance(item, list):
            indexes.extend(find_all_element_in_nested_list(item, element_to_find, index + [i]))
    return indexes

def access_element_by_indices(data, indices):
    try:
        for index in indices:
            data = data[index]
        return data
    except (IndexError, TypeError):
        return None




#Scaffolding:



A=[3]
P=[]
A_novo = []

for i in range(len(A)):
    result_lists = []
    K=copy.deepcopy(C)
    
    for j in range(len(A[i])):
        for x in range(len(K)):
            if j < len(A[i])-1:
                if A[i][j] in K[x]:
                    #K.remove(K[x])
                    K[x] = 'a'
                else:
                    pass
            else:
                if A[i][j] in K[x]:
                    K[x].remove(A[i][j])
                    P.extend(K[x])
                else:
                    pass
    print(f'P={P}')
    

    for p_element in P:
        new_list = A.copy()  # Create a copy of A
        new_list.append(p_element)  # Append one element from P to the copy of A
        result_lists.append(new_list)  # Add the new list to the result
    
    A_novo.extend(result_lists)

A = A_novo

print(f'A={A}')
            


