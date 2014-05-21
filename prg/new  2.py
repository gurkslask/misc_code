import smtplib  
import threading
import time
import rpi.GPIO as GPIO

class Button(threading.Thread):
	"""Skapa tr�d som moniterar ing�ng"""
	
	def __init__(self, channel):
		threading.Thread.__init__(self)
		self._pressed = False
		self.channel = channel
		
		#deklarera pin som ing�ng
		GPIO.setup(self.channel, GPIO.IN)
		
		#Avsluta tr�den n�r programmet �r f�rdigt
		self.daemon = True
		
		#Starta tr�den 
		self.start()
	def pressed(self):
		if self._pressed:
			#Rensa flaggan n�r vi har uppt�ck flank
			self._pressed = False
			return True
		else:
			return False
	
	def run(self):
		previous = None
		while 1:
			#L�s ing�ngskanalen
			current = GPIO.input(self.channel)
			time.sleep(0.01) #10
			
			#Kolla n�r signalen g�r fr�n 1 till 0
			if current == False and previous == True:
				self._pressed = True
				
				#F�rdr�jning p� �terst�ll flagga
				while self._pressed:
					time.sleep(0.05) #50 ms
			
			previous = current
			
def onButtonPress():
	print("Knappen har blivit tryckt")
	#Send_Gmail()
	
#Skapa en knapp tr�d f�r knapp p� pin "11"
button = Button(11)

while True:
	#Fr�ga efter namn och s�g hello
	name = input("Enter a name (or Q to quit): ")
	if name.upper() == ('Q'):
		break
	print("Hello", name)
	#Kolla om knappen blivit tryckt
	if button.pressed():
		onButtonPress()


		
	
	
				
  

  
  
 
  
# The actual mail send
def Send_Gmail():
	fromaddr = 'fromuser@gmail.com'  
	toaddrs  = 'touser@gmail.com'  
	msg = 'There was a terrible error that occured and I wanted you to know!'  
	# Credentials (if needed)  
	username = 'username'  
	password = 'password' 

	server = smtplib.SMTP('smtp.gmail.com:587')  
	server.starttls()  
	server.login(username,password)  
	server.sendmail(fromaddr, toaddrs, msg)  
	server.quit()  
