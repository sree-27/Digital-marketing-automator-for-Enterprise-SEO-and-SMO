
import pickle
class Book():
    authorname="anu"
    authoremail="anu@gmail"
    authorphone="8456111"
    def add(self):
       
        file=open("C:/Users/Admin/Desktop/python/ourbook","wb")
        pickle.dump(Book,file)
        

        file.close()
    def read(self):
        file=open("C:/Users/Admin/Desktop/python/ourbook","rb")
        pickle.load(file)

        file.close()
        print(Book.authorname)
        print(Book.authoremail)
        print(Book.authorphone)
obj=Book()
obj.add()
obj.read()

obj2=Book()
obj2.add()
obj2.read()
