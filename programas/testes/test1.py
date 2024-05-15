def nested_list(A, depth=None, length=None):
    if depth is None:
        depth = len(A)
    if length is None:
        length = A[-1]

    if depth == 1:
        return [0] * A[0]
    else:
        my_list = []
        return [nested_list(A, depth=depth-1, length=A[-depth]) for _ in range(length)]


A= [[1,1,5],
	[1,4,13],
	[3,2,12]]
B= [[-22,2,7],
	[-27,3,8],
	[10,-1,-3]]

AB = nested_list([len(B[0]), len(A)])
for i in range(len(A)):
	for j in range(len(B[0])):
		for k in range(len(B)):
			AB[i][j] = AB[i][j] + A[i][k]*B[k][j] 

for _ in range(len(AB)):
	print(AB[_])