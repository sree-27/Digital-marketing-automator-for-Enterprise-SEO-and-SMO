def sum(a,b):	
	print(a+b)
def diff(a,b):
	print(a-b)
def mult(a,b):
	print(a*b)
def div(a,b):
	print(a/b)
def inputdetails():

	a=int(input("enter the first number="))
	b=int(input("enter the second number="))
	choice=mychoice()
	if(choice==1):
		sum(a,b)
	elif(choice==2):
		diff(a,b)
	elif(choice==3):
		mult(a,b)
	elif(choice==4):
		div(a,b)
	else:
		print("invalid")

def mychoice():
	print("1.addition")
	print("2.subtraction")
	print("3.multiplication")
	print("4.division")
	choice=int(input("enter choice="))
	return choice

	

inputdetails()
mychoice()

	