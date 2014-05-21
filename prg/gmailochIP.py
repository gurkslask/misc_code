import smtplib
import socket
server=smtplib.SMTP('smtp.gmail.com:587')
gmail_acc = 'alexander.svensson.x'
server.starttls()
server.login('alexander.svensson.x', 'Fyrtio22')
msg='\n'+str(socket.gethostbyname(socket.gethostname()))
server.sendmail(gmail_acc+'@gmail.com', 'gurkslask@gmail.com', msg)
