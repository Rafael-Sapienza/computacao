#receber lista do usuario
input_String = input('Enter elements of a list separated by space: ')
user_List = input_String.split()
print('list: ', user_List)

#receber nova ordenacao do usuario
input_Order = input('select new order:')
new_Order_List = input_Order.split()
print(new_Order_List)

Int=[]
new_List=[]
#´Numero de termos não podem ser diferentes
if len(new_Order_List) != len(user_List):
	print('invalid inputs')


#else
else:
	x=0
	while x < len(new_Order_List):
		Int.append(int(new_Order_List[x]))
		x=x+1
		if x == len(new_Order_List):
			print('x1: ', Int)
#ordencoes com numeros>len(Int)-1 ou <0 nao sao validas
	#for y in range(len(Int)):
	y = 0
	while y < len(Int):
		if y not in Int:
			print('invalid inputs')
		else:
			new_List.append(user_List[Int[y]])
			if y==len(Int)-1:
				print('x2: ', new_List)
		y = y + 1

'''for i in range(len(Int)):
		new_List.append(user_List[Int[i]])
	print(new_List)'''


			



 
