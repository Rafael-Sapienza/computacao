#imports 
import copy

#functions
def inputHead():
	A=[int(r) for r in input().split()]
	return A

def inputBody():
	B=[]
	for _ in range(M):
		B.append([int(r) for r in input().split()])
	return B

def getPath(B):
	C=[]
	for i in range(len(B)):
		C.append(B[i][0:2])
	return C

def getTime(B):
	T=[]
	for i in range(len(B)):
		T.append(B[i][2])
	return T

def getInitialPossiblePaths(D):
	P=[]
	for i in range(len(C)):
		if D in C[i]:
			j = C[i].index(D)
			print(f'i = {i} , j = {j}')
			C[i].remove(C[i][j])
			.append(C[i])
			#C.remove(C[i])	
	for i in range(len(P)):
	C.remove(P[i])
	return P, C

def getPossiblePaths():
	for x in range(len(A)):
		print(f'x={x}')
		B=[]
		#K=C.copy() 
		K = copy.deepcopy(C)
		print(f'K={K}')
		for i in range(len(K)):
			if A[x][0] in K[i]:
				j = K[i].index(A[x][0])
				print(f'i = {i} , j = {j}')
				K[i].remove(K[i][j])
				print(f'K={K}')
				B.append(K[i])
		A[x].append(B)
	return A

A = inputHead()
B = inputBody()
C = getPath(B)
T = getTime(B)
getInitialPossiblePaths(D)

N , M, D = A
print(f'A={A}')
print(f'C={C}')
print(f'A={A}')
print(f'B={B}')
print(f'A={A}')









'''	
for i in range(len(A)):
	C.remove(A[i])
'''


			



