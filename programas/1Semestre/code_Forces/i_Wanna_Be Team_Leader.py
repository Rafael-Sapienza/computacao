
n,m = [int(r) for r in input().split()]

A = [int(r) for r in input().split()]

7 5 9B = [int(r) for r in input().split()]


def programmers_for_ith_project(i,A,B):
	possible_Programmers=[]
	for k in range(1,len(A)+1):
		for j in range(len(A)):
			if A[j] >= B[i]/k:
				possible_Programmers.append(j)
		
		if len(possible_Programmers) >= k:
			possible_Programmers=possible_Programmers[0:k+1]

			data=[]
			data.append(k)

			data.extend(possible_Programmers)

			print(data)

			return data

			break

#print(programmers_for_ith_project(i=0,A=[4,6,100,5,1],B=[50,1,12]))



def remove_used_programmers(data,A):
	possible_Programmers = data[1:]
	
	for i in possible_Programmers:
		A[i] = -1



A=[4,6,100,5,1]
B=[50,1,12]



def recursion(A,B):
	for i in range(len(B)):
		programmers_for_ith_project(i,A,B)
		remove_used_programmers(programmers_for_ith_project(i,A,B),A)

recursion(A,B)