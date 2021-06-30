import os
def deletefile():
    try:
        os.remove("C:/Users/Admin/Desktop/python/document/book.py")
    except:
        print("file does not exist")

def deletefolder():
    try:
        os.remove("C:/Users/Admin/Desktop/python/document/book.py")
        os.rmdir("C:/Users/Admin/Desktop/python/document/book.py")
    except:
        print("folder does not exist")



def deletefolders():
    if os.path.exists("C:/Users/Admin/Desktop/python/document/book"):
        os.rmdir("C:/Users/Admin/Desktop/python/document/book")
    else:
        print("folder does not exist")
deletefolders()