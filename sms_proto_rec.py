import serial
from curses import ascii
# since we need ascii code from CTRL-Z
import time

def sendSMS(phonenumber,msg):
	SMS = "Esto es una prueba"
	ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=1)
	# 460800 is baud rate, ttyUSB0 is virtual serial port we are sending to
	ser.write("AT\r\n")
	time.sleep(0.5)
	# send AT to the ttyUSB0 virtual serial port
	line = ser.readline()
	print(line)
	# what did we get back from AT command? Should be OK
	ser.write("AT+CMGF=1\r\n")
	time.sleep(0.5)
	# send AT+CMGF=1 so setting up for SMS followed by CR 
	line = ser.readline()
	#print(line)
	# what did we get back from that AT command?
	ser.write('AT+CMGS="%s"\r\n' %phonenumber)
	time.sleep(0.5)
	# escribimos el texto del mensaje
	ser.write(msg+ascii.ctrl('z'))
	time.sleep(0.5)
	#time.sleep(2)
	# send AT+CMGS then CR, then phonenumber variable
	#ser.write(SMS)
	# send the SMS variable after we sent the CR
	#ser.write(ascii.ctrl('z'))
	# send a CTRL-Z after the SMS variable using ascii library
	time.sleep(10)
	# wait 10 seconds
	line += ser.readline()
	line += ser.readline()
	line += ser.readline()
	line += ser.readline()
	#print ser.readline()
	#print ser.readline()
	#print ser.readline()
	#print ser.readline()
	print(line)
	# borramos mensajes recibidos
	ser.write("AT+CMGD=2\r\n")
	line = ser.readline()
	print(line)

######### MAIN ###########################################
#listaMSISDN = open("listTelrec.txt","r")
# loop  y leo linea por linea para disparar SMS
while(True):
	try:
		listaMSISDN = open("listTelrec.txt","r")
		for reg in listaMSISDN:
			linea,msg = reg.split("|")
			sendSMS(linea.rstrip('\n'),msg.rstrip('\n'))
		listaMSISDN.close()
		time.sleep(600)
	except KeyboardInterrupt:
		listaMSISDN.close()
		print("Se ha interrumpido script por teclado")
		exit(0)
	finally:
		listaMSISDN.close()
