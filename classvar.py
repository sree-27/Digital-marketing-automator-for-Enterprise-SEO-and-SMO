class Car :
    gear=0

    def __init__(self,uname, upass):
       
        self.username = uname
        self.password = upass
        print("object initialized with init fuction,instance variables uname and pasword are declared and initilized with uname and upass",uname,upass)

    def changeGear(self,gearvalue) :
        self.gear=gearvalue
        print("function called -value of gear based on gearvalue passed",self.gear)

print("class variable value of gear: ",Car.gear) 

print("object benz created and initilaized using init" )

benz=Car("akhil","pa123")
print("value of gear in benz : ",benz.gear)
benz.changeGear(1)
print("value of gear in benz : ",benz.gear)

print("object bmz created and initilaized using init" )

bmw=Car("anu","an435")
print("value of gear in benz : ",bmw.gear)
bmw.changeGear(2)
print("value of gear in benz : ",benz.gear)

print("class variable value of gear: ",Car.gear)
 
print("instance variable value of gear in benz: ",benz.gear) 

print("instance variable value of gear in bmw: ",bmw.gear) 

print("instance variable uname and upass  in benz: ",benz.password,benz.username) 

print("instance variable uname and upass  in bmw: ",bmw.password,bmw.username) 