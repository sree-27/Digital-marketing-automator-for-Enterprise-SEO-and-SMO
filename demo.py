class demo():
	count=0
	def __init__(self,rollno,name):
		self.rollno=rollno
		self.name=name
		demo.count+=1
	def view(self):
		print(self.rollno)
		print(self.name)

demoaadhi=demo(1,"aadhi")
demoabhi=demo(2,"abhi")

demoaadhi.view()
demoabhi.view()
print("total number of objects created:",demo.counter)