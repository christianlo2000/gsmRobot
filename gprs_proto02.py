#############################################################
# Script....: gprs_proto02.py
# Objetivo..: ejecutar protocolo de GPRS con modem 3g o 4g 
#             en forma automatica
# diferencia: respecto de gprs_proto01.py, que el archivos de urls
#             posee dos campos, el segundo tiene duracion de la 
#             navegacion.
#############################################################
import logging
import threading
import time
import webbrowser, os, sys
import subprocess

# Funciones y metodos
def navegarEnPag(url,tiempo):
	chrome_path = '/usr/lib/chromium-browser/chromium-browser'
	webbrowser.get(chrome_path).open(url)
	time.sleep(tiempo)
def finNavegacion():
	os.system("ps -ef | grep chrom | grep -v grep | awk '{print $2}' | xargs kill")
def speedTest():
	#while(True):
	infoSpeed = subprocess.check_output("speedtest-cli | egrep \"Download|Upload\" | grep -v grep",shell=True)
	print("SPEEDTEST")
	print(infoSpeed)
	#time.sleep(.1)
		#os.system("clear")
def clearDownload():
	os.system("rm /home/pi/Downloads/*")
######### MAIN ###########################################
listaURL = open("urls.txt","r")
# loop  y leo linea por linea para disparar navegacion GPRS
try:
	#x = threading.Thread(target = speedTest, args = ())
	#x.start()
	for linea in listaURL:
		msisdn,dur = linea.split("|")
		speedTest()
		navegarEnPag(msisdn.rstrip('\n'),float(dur))
		#speedTest()
finally:
	listaURL.close()
	finNavegacion()
	clearDownload()
	speedTest()
	print("Fin ejecucion pruebas de datos")	
