class Mylibrary:
    def __init__(self,bookname,bookauthor):
        self.mybookname=bookname
        self.myauthor=bookauthor
        print("my library object created with instance variable mybookname and mybookauthor")

mylib=Mylibrary("magic parameter","jeorge")
mylibs=Mylibrary("youth trender","wilson")
print(mylib.mybookname,mylib.myauthor)
print(mylibs.mybookname,mylibs.myauthor)

librarylist=[]

librarylist.append(mylibs)
librarylist.append(mylib)

print("arrayofobjects librarylist created with two objects mylib in position 0 and mylibs in position 1")

for i in librarylist:
    print(i.mybookname,i.myauthor)
