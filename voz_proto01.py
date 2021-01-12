#############################################################
# script....: voz_proto01.py
# Objetivo..: ejecutar protocolos de voz con modem usb 3g o 4g
# Parametros: no requiere
# Estado....: Codigo funciona OK pero falta manejo de excepciones
#############################################################
import serial
from curses import ascii
# since we need ascii code from CTRL-Z
import time

def makeCall(phonenumber):
	ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=1)
	# 460800 is baud rate, ttyUSB0 is virtual serial port we are sending to
	ser.write("AT\r\n")
	# send AT to the ttyUSB0 virtual serial port
	line = ser.readline()
	print(line)
	# llamamos a numero destino
	comandoATD = "ATD+"+phonenumber+";\r\n"
	ser.write(comandoATD)
	line = ser.readline()
	print(line)
	# hacemos pausa de varios segundos, hc 15 segundos
	time.sleep(15)
	# Colgamos llamada
	ser.write("ATH\r\n")
	time.sleep(10)
	# wait 10 seconds
	print ser.readline()
	print ser.readline()
	print ser.readline()
	print ser.readline()

######### MAIN ###########################################
listaMSISDN = open("listTelVoz.txt","r")
# loop  y leo linea por linea para disparar SMS
try:
	for linea in listaMSISDN:
		makeCall(linea.rstrip('\n'))
finally:
	listaMSISDN.close()
