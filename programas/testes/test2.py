X = [[2,5],[2,3]]
Y = [[4,1],[4,2]]
meteors_Position = [ [ [1,2],[3,3] ] ,[ [1,1],[2,2],[3,3] ] ]



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



print(fallen_meteors_in_ith_farm(2))