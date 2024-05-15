#Receber input:
def treatInput():
	A = '0 0 0 0'
	cont = 2
	i = 0
	while True:
		B = input()
		if len(B) != 0 or i > cont:
			if len(B) != 0:
				A = B.strip()
			break
		i = i + 1
	return A

def get_farms_coordinates(A):
	global X, Y
	
	X.append([A[0],A[2]])
	Y.append([A[1],A[3]])

def get_meteors_coordinates():
	global meteors_Position

	M=[]
	N=int(treatInput())
	for _ in range(N):
		C=[int(r) for r in treatInput().split()]
		M.append(C)
	if meteors_Position == []:
		meteors_Position = M
	else:
		meteors_Position = [meteors_Position, M]
	#return meteors_Position
	
def get_input(A = None):
	global X, Y, meteors_Position

	if A is None:
		A = [int(r) for r in treatInput().split()]

	else:
		if A != [0,0,0,0]:
			get_farms_coordinates(A)
			get_meteors_coordinates()
			#print(meteors_Position)
			B = [int(r) for r in treatInput().split()]
			get_input(A = B)
		else:
			return(X, Y, meteors_Position)

# Fazer os cálculos com base nos inputs:
def is_meteor_in_farm(m1, m2, x1, x2, y1, y2):
	if m1<=x2 and m1>=x1 and m2<=y1 and m2>=y2:
		return True
	else:
		return False

def fallen_meteors_in_ith_farm(i):
	i=i-1 #primeira fazenda corresponde a i = 0
	k = 0
	x1,x2  = X[i]
	y1,y2 = Y[i]
	for n in range(len(meteors_Position[i])):
		m1,m2 = meteors_Position[i][n]
		if is_meteor_in_farm(m1, m2, x1, x2, y1, y2):
			k += 1
		else:
			pass
	return k

def final_result():
	for i in range(len(X)): #iterando pelo número de fazendas
		print(f'Teste {i+1}')
		print(f'{fallen_meteors_in_ith_farm(i+1)}')


'''
res = ''
cont = 0
while res != '0 0 0 0':
	res = treatInput()
	print(cont, ': ', res)
	cont = cont + 1

print('acabou!')
'''

#chamadas de função
X = []
Y = []
meteors_Position = []

get_input()
final_result()