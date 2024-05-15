class Person:
	def __init__(s,name,age):
		s.n = name
		s.a = age
	
	def __str__(abc):
		return f'{abc.n}:({abc.a})'
	
	def printname(abc):
		return f'{abc.n}+{abc.a}'

class Student(Person):
	def __init__(s,fname,lname, year):
		super().__init__(lname,fname)
		s.graduate = year

	def prin(abc):
		return f'Hello, my name is {abc.a}; I am {abc.n} years old and i graduated in {abc.graduate}!' 

	def __str__(abc):
		return f'Sim,{abc.a},{abc.n}'

p1=Person('john',36)
p2=Student('joao', 18, 2000)