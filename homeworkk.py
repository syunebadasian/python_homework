import math
pi=math.pi
# #Task1
class Circle:
	def __init__(self,r):
		self.r=r
	def area(self,r):
		S=pi*r**2 
		return S
	def circumference(self,r):
	    C=2*pi*r	
	    return C 
circle=Circle(6)
print(circle.area(6))	
#Task2
class Sum:
	def __init__(self):
		self.numbers=[10,20,10,40,50,60,70]
		self.target= 50
	def check(self):
	    for i in range(len(self.numbers)):
	        for j in range(len(self.numbers)):
	            b=self.numbers[i]+self.numbers[j]
	            if b == self.target:
	                print(i,j)
	                break
orange=Sum()
orange.check()	                
	                	
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

#Task4
class Country:
	def __init__(self,name,continent):
		self.name=name
		self.continent=continent
	def presentation(self):
		print(f"The name of a country is {self.name} located in {self.continent}")

class Brand:
	def __init__(self,brand_name,start_date):
		self.brand_name=brand_name
		self.start_date=start_date
	def presentation_brand(self):
	    print(f"{self.brand_name} is an armenian brand that was founded in {self.start_date}")

class Season:
	def __init__(self,season_name,average_temp):
		self.season_name=season_name
		self.average_temp=average_temp
	

class Product(Country,Brand,Season):
	def __init__(self,product_name,price,name,continent,brand_name,start_date,season_name,average_temp,discount):
		self.product_name=product_name
		self.price=price
		self.discount=discount
		Country.__init__(self,name,continent)
		Brand.__init__(self,brand_name,start_date)
		Season.__init__(self,season_name,average_temp)

	def discount_presentation(self):
	    c=int(self.price * self.discount)/100
	    self.price -= c

	
	def mixed_presentation(self):
		self.presentation()
		self.presentation_brand()
		self.discount_presentation()


		
		print(f"The name of a country is {self.name} located in {self.continent}. {self.brand_name} is an armenian brand that was founded in {self.start_date}. Recently {self.brand_name} release a new product called {self.product_name}. This product mainly designed for {self.season_name} use , when the average temperature is approximately under - {self.average_temp}. Using {self.product_name} women can have a clear and moist skin even in a cold weather. Now the product is {self.discount}% off and you get it for only {self.price}. ")

product=Product("Winter Garden",50,"Armenia","Western Asia","Nairian",2012,"Winter",8.4,50)
product.mixed_presentation()

#Task5

class Hotel:
	def __init__(self,name,place,mid,midprice,lux,luxprice,discount_hotel):
		self.name=name
		self.place=place
		self.mid=mid
		self.midprice=midprice
		self.lux=lux
		self.luxprice=luxprice
		self.discount_hotel=discount_hotel


	def presentation(self):
	    print(f"We will stay at {self.name} hotel which is located near the {self.place}. We offer 2 types of rooms: \n middle - {self.midprice} AMD \n lux - {self.luxprice} AMD.")	


  def booking(self):
  	check=True
    while check:
    	booking=input("Which type of room do you want. 1 for mid , 2 for lux")
    	if booking=="1":
    		print(f"The price of a room is {self.midprice}")
    		
    		
    	elif booking=="2":
    	    print(f"The price of a room is {self.luxprice}")

  	class Taxi:
	def __init__(self,taxi_name,car_types,price_tour,discount_taxi):
		self.taxi_name=taxi_name
		self.car_types=car_types
		self.price_tour=price_tour
		self.discount_taxi=discount_taxi

	def presentation_taxi(self):
	    print(f"{self.taxi_name} company provides {self.car_types} cars and the price for it is {self.price_tour}")	

	def price_discount(self):
	    print(f"Old price for tour is {self.price_tour} AMD")
	    price=int(self.price_tour*self.discount_taxi)/100
	    self.price_tour-=price
	    print(F"Discounted price for car is {int(self.price_tour)}.") 
bmw=Taxi("Ride over","BMW", 10000,10)
print(bmw.price_discount())

class Tour(Hotel,Taxi):
    def __init__(self,name,place,mid,midprice,lux,luxprice,discount_hotel,taxi_name,car_types,price_tour,discount_taxi,tourname,price_lux,price_mid):
        Hotel.__init__(self,name,place,mid,midprice,lux,luxprice,discount_hotel)
        Taxi.__init(slef,taxi_name,car_types,price_tour,discount_taxi)
        self.tourname=tourname
        self.price_lux=price_lux
        self.price_mid=price_mid

    def mixed_presentation(self):
        print(f"Hello we offer {self.tourname},we have two options:{self.price_lux} and {self.price_mid} which includes {self.presentation_taxi()} {self.presentation()}")    

tour=Tour("Lerane","Geghard",{"room1":"free","room2":"free","room3":"busy"},20000,{"room1":"free","room2":"busy","room3":"busy"},40000,10,"Ride Over","BMW",10000,10,"Geghard tour",50000,30000)

tour.mixed_presentation()

# task6

class Temp():
	def __init__(self,curr_temp,goal_temp):
		self.curr_temp=curr_temp
		self.goal_temp=goal_temp
	def get(self):
		return self.curr_temp

	def set(self,new):
		self.__curr_temp=new

	def check(self):
		if self.__curr_temp==self.goal_temp:
			return True
		else:
		  return False	

a=Temp(20,22)
print(a.get())
a.set(30)
print(a.get())
print(a.check())	

b = Temp(24,24)
c = Temp(27,26)
d = Temp(22,22)

#task7
import os 

os.chdir("/Users/M.Ch/Desktop/Syune/new_python_folder/")
os.mkdir("Dir1")
print(os.getcwd())
os.chdir("/Users/M.Ch/Desktop/Syune/new_python_folder/Dir1/")
os.mkdir("Dir2")
os.makedirs("Dir3/Dir4")
print(os.getcwd())
question = input("Do you want to delete folders ? yes/no \n")
if question=="yes":
	os.chdir("/Users/M.Ch/Desktop/Syune/new_python_folder/Dir1/Dir3/")
	os.rmdir("Dir4")
	os.chdir("/Users/M.Ch/Desktop/Syune/new_python_folder/Dir1/")
	os.rmdir("Dir3")
	os.rmdir("Dir2")
	os.chdir("/Users/M.Ch/Desktop/Syune/new_python_folder")
	os.rmdir("Dir2")
else:
	pass

# task8
import json

dic = {
	"name": "Syune Badasian",
	"Age": 18,
	"ID":"273826868"
	}
json=json.dumps(dic,indent=2)

with open("py.txt","w") as f:
	f.write(json)

#task9
import json
import os
import requests
import time
import concurrent.futures

img_urls=[
"https://images.unsplash.com/photo-1498330177096-689e3fb901ca?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
"https://images.unsplash.com/photo-1559827260-dc66d52bef19?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
"https://images.unsplash.com/photo-1505118380757-91f5f5632de0?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
"https://images.unsplash.com/photo-1501436513145-30f24e19fcc8?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
"https://images.unsplash.com/photo-1542228556-0125288e633d?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
"https://images.unsplash.com/photo-1525700165215-df2db783147a?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
"https://images.unsplash.com/photo-1514814309075-1f08d9a71f4c?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
"https://images.unsplash.com/photo-1534533816365-488568ee03eb?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
"https://images.unsplash.com/photo-1516383523534-0186f80e0b62?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
"https://images.unsplash.com/photo-1514415008039-efa173293080?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
]

t1=time.perf_counter()

def download_image(img_urls):
	img_bytes=requests.get(img_urls).content
	img_name=img_url.split("/")[3]
	img_name=f"{img_name}.jpg"
	with open(img_name,"wb") as img_file:
		img_file.write(img_bytes)
		print(f"{image_name} was downloaded...")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image,img_urls)

t2=time.perf_counter()








  
	        	




