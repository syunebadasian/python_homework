import math
pi=math.pi
#Task1
class Circle:
	def __init__(self,r):
		self.r=r
	def area(self):
		S=pi*r**2 
		return S
	def circumference(self):
	    C=2*pi*r	
	    return C 
circle=Circle(5)
print(circle.Circle())	
#Task2
class Sum:
	def __init__(self,numbers,target):
		self.numbers=numbers
		self.target=target
		new_dict={}
		for i,numbers in enumerate(numbers):
			if target - numbers in new_dict:
#Task3
class Person:
	def __init__(self,age):
		self.age=age

class Student(Person):
	def __init__(self,name,specialty,age):
		self.name=name
		self.specialty=specialty
		Person.__init__(self,age)
student=Student("Jane","doctor",28)	
print("Student's name is",student.name,"She is a",student.specialty,"Her age is",student.age)


