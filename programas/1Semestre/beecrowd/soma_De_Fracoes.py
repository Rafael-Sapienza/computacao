a,b,c,d=[int(r)for r in input().split()]

def is_triangle(a,b,c):
	if a<b+c and b<a+c and c<a+b:
		return True
	else:
		return False


def is_possible_to_find_triangle(a,b,c,d):
	if is_triangle(a,b,c) or is_triangle(a,b,d) or is_triangle(a,c,d) or is_triangle(b,c,d):
		print('S')
	else:
		print('N')

is_possible_to_find_triangle(a,b,c,d)
