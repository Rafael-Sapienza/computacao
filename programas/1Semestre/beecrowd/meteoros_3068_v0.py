#Receber input:

def get_farms_coordinates(A):
	global X, Y
	
	X.append([A[0],A[2]])
	
	Y.append([A[1],A[3]])



def get_meteors_coordinates():
	global meteors_Position

	M=[]

	N=int(input())

	for _ in range(N):
		C=[int(r) for r in input().split()]
		M.append(C)

	if meteors_Position == []:
		meteors_Position = M

	else:
		meteors_Position = [meteors_Position, M]

	#return meteors_Position




	
X = []
Y = []
meteors_Position = []



def get_input(A = [int(r) for r in input().split()]):
	global X, Y, meteors_Position
		

	if A != [0,0,0,0]:
		
		get_farms_coordinates(A)
		get_meteors_coordinates()

		#print(meteors_Position)

		B = [int(r) for r in input().split()]

		get_input(A = B)


	else:
		return(X, Y, meteors_Position)



get_input()



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



final_result()