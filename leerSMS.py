import serial
from curses import ascii
# since we need ascii code from CTRL-Z
import time

def readSMS():
	ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=1)
	# 460800 is baud rate, ttyUSB0 is virtual serial port we are sending to
	ser.write("AT\r\n")
	time.sleep(0.5)
	# send AT to the ttyUSB0 virtual serial port
	line = ser.readline()
	print(line)
	# leer mensajes ya leidos
	#print("AT+CMGL=\"REC READ\"")
	# leer mensajes no leidos
	#print("AT+CMGL=REC UNREAD")
	# leer toods los mensajes
	print("AT+CMGL=ALL")
	# leer un mensaje por id
	#print("AT+CMGR=1")
	time.sleep(0.5)
	line = ser.readline()
	print(line)

######### MAIN ###########################################
# loop  y leo linea por linea para disparar SMS
while(True):
	try:
		print("Leemos SMS pendientes ...")
		readSMS()
		time.sleep(5)
	except KeyboardInterrupt:
		print("Se ha interrumpido script por teclado")
		exit(0)
