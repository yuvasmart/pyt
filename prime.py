n=input()
n=int(n)
f=0
if(n>1):
	for i in range(2,n):
		if(n%i==0):
			f=1
	if(f==1):
	    print("no")
	else:
	    print("yes")
else:
	print("enter correct number")
