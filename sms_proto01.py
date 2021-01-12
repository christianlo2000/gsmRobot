import serial
from curses import ascii
# since we need ascii code from CTRL-Z
import time

def sendSMS(phonenumber):
	SMS = "Esto es una prueba"
	ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=1)
	# 460800 is baud rate, ttyUSB0 is virtual serial port we are sending to
	ser.write("AT\r\n")
	# send AT to the ttyUSB0 virtual serial port
	line = ser.readline()
	print(line)
	# what did we get back from AT command? Should be OK
	ser.write("AT+CMGF=1\r\n")
	# send AT+CMGF=1 so setting up for SMS followed by CR 
	line = ser.readline()
	print(line)
	# what did we get back from that AT command?
	ser.write('AT+CMGS="%s"\r\n' %phonenumber)
	# send AT+CMGS then CR, then phonenumber variable
	ser.write(SMS)
	# send the SMS variable after we sent the CR
	ser.write(ascii.ctrl('z'))
	# send a CTRL-Z after the SMS variable using ascii library
	time.sleep(10)
	# wait 10 seconds
	print ser.readline()
	print ser.readline()
	print ser.readline()
	print ser.readline()

######### MAIN ###########################################
listaMSISDN = open("listTel.txt","r")
# loop  y leo linea por linea para disparar SMS
try:
	for linea in listaMSISDN:
		sendSMS(linea.rstrip('\n'))
finally:
	listaMSISDN.close()
