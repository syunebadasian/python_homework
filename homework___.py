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
