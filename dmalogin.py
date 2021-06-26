def myfile():
    try:
        filename=input("enter file name: ")
        doc=open("C:/Users/anuzd/Desktop/python/file/"+filename,"x")
        filedata=input("enter details to write into the file")
        doc.write(filedata)
        doc.close()
    except:
        print("file already exisit")
        filename=input("enter new file name")

        doc=open("C:/Users/anuzd/Desktop/python/file/"+filename,"x")
        filedata=input("enter details to write into the file")
        doc.write(filedata)
        doc.close()

    
    doc=open("C:/Users/anuzd/Desktop/python/file/"+filename,"r")
    print(doc.read())
    doc.close()
    
myfile()