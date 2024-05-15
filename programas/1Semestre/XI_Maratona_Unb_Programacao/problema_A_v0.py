import copy
#inputs:


A=[int(r) for r in input().split()]

N , M, D = A

B=[]
for _ in range(M):
	B.append([int(r) for r in input().split()])

print(B)


C=[]
for i in range(len(B)):
	C.append(B[i][0:2])

print(C)


'''
for i in range(len(C)):
	C[i].sort()

for i in range(len(B)):
	B[i][0:2]=C[i]
'''

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


#Scaffolding


A=[D]
E=[]
for x in range(len(A)):
	B=[]
	if find_all_element_in_nested_list(data = C, element_to_find = D):
		results = find_all_element_in_nested_list(data = C, element_to_find = D)
		for i in range(len(results)):	
			
			l0 = results[i]
			l1 = results[i].pop()
			l2 = results[i][:-2]
			

			access_element_by_indices(data = C, indices = l1).remove(access_element_by_indices(data = C, indices = l0))
			B.extend(access_element_by_indices(data = C, indices = l1))
			access_element_by_indices(data = C, indices = l2).remove(access_element_by_indices(data = C, indices = l1))
		A[x].append(B)
		E.append(C)

#C=E




'''
A=[]
for i in range(len(C)):
	if D in C[i]:
		j = C[i].index(D)
		print(f'i = {i} , j = {j}')
		C[i].remove(C[i][j])
		A.append(C[i])
		#C.remove(C[i])		

print(f'A={A}')



for i in range(len(A)):
	C.remove(A[i])


print(f'C={C}')

'''


E=[]
for x in range(len(A)):
	print(f'x={x}')
	B=[]
	#K=C.copy() 
	K = copy.deepcopy(C)

	if find_all_element_in_nested_list(data = K, element_to_find = A[x][0]):
		results = find_all_element_in_nested_list(data = K, element_to_find = A[x][0])

		for i in range(len(results)):
			l0 = results[i]
			l1 = results[i].pop()
			l2 = results[i][:-2]
			access_element_by_indices(data = K, indices = l1).remove(access_element_by_indices(data = K, indices = l0))
			B.extend(access_element_by_indices(data = K, indices = l1))
			access_element_by_indices(data=K, indices = l2).remove(access_element_by_indices(data = K, indices = l1))

		A[x].append(B)
		E.append(K)

	
print(f'E={E}')






#E is possible paths, A is where he goes


'''
#E=[]
for x in range(len(A[x])):
	for y in range(A[x][1]):
		print(f'x={x}')
		L = copy.deepcopy(E)
		for i in range(len(L[x])):
			if A[x][1][y][0] in L[x][i]:
				j = L[i].index(A[x][0])
				print(f'i = {i} , j = {j}')
				K[i].remove(K[i][j])
				print(f'K={K}')
				B.append(K[i])
		A[x].append(B)
		for i in range(len(A[x][1])):
			K.remove(A[x][1][i])
		E.append(K)
'''







