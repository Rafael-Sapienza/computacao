a,b,c = [int(r) for r in input().split()]

Possibilidades= [-1,1,0]


def can_go_back_to_present(a,b,c):
	result = False
	for k1 in Possibilidades:
		for k2 in Possibilidades:
			for k3 in Possibilidades:
				if k1*a+k2*b+k3*c == 0 and (k1!=0 or k2!=0 or k3!=0):
					result=True 
	return result 




def print_result(a,b,c):
	if can_go_back_to_present(a,b,c):
		print('S')

	else:
		print('N')


print_result(a,b,c)
