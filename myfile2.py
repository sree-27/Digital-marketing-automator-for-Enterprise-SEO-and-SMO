class Studentdetails():
    def createfile(self):
        filename=input("enter file name:")
        try:
           
            detailscount=input("enter the number students to be registered")
            myfile=open("C:/Users/Admin/Desktop/python/document/"+filename,"a")
            name=input("enter your name")
            age=input("enter your age")
            myfile.write("name="+name+"\n"+"age="+age)
            myfile.close()
        except:
            print("error")
    def fileread(self):
        filename=input("enter file name:")
        try:
            myfile=open("C:/Users/Admin/Desktop/python/document/"+filename,"r")
            print(myfile.read())
        except:
            print("error")


obj=Studentdetails()
obj.createfile()



