class Library:
	def registration(self):
		print("welcome to regisration.")
	def searchbook(self,bookid):
		print("hai,helloo")
		if(bookid>=60):
			print("Book isavaiable.")
		else:
			print("Book is not availiable.")
	def searchuser(self):
		n=int(input("enter a mobile number"))
		if(n==9448708768):
			print("user found")
		else:
			print("user not found")

class Digitallibrary(Library):
	def scanqrcode(self):
		print("qr code")

class Aidigitallibrary(Digitallibrary):
	def aianalysis(self):
		print("welcome to regisration.")

lourddigitallibrary=Aidigitallibrary()

lourddigitallibrary.registration()
lourddigitallibrary.searchbook(60)
lourddigitallibrary.searchuser()

lourddigitallibrary.scanqrcode()

lourddigitallibrary.aianalysis()
