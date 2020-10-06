#tasl1
import random
a=str(random.randint(1000,9999))
lst=[]
cow=0
for i in a:
	lst.append(i)

while cow<4 and exit !="x":
	x=str(input("Choose a 4 digit number,x to exit:"))
	xlst=[]
	cow=0
	bull=0
	if x!="x":
		for i in x:
			xlst.append(i)
		for i in lst:
		    if i in xlst and lst.index(i)==xlst.index(i):
		       cow+=1
		    if i in xlst and lst.index(i)!=xlst.index(i):
		        bull+=1
		print(cow,"cow(s)",bull,"bull(s)")
		
print(lst,xlst)

#task2
x={'1':['a','b'],'2':['c','d']}
list1=x.get('1')
list2=x.get('2')
    for i in range(2):
    	for j in range(2):
    		print(list1[i]+list2[j])