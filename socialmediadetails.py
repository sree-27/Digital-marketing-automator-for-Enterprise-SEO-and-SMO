import sys
sys.path.insert(1,'C:/Users/Admin/Desktop/python')
from mymodule import Mymodule 
import mymodule
class Studentdetails:

    def moduledetails(self):

        l=Mymodule.name
        print("name:",l)
        m=Mymodule().student
        print("student details:",m)
        k=mymodule.teacher
        print("teacher details:",k)
        t=mymodule.address
        print("address:",t)
stud=Studentdetails()
stud.moduledetails()