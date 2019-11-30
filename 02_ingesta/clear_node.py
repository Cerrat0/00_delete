import os
from time import sleep

#bucle while para borrar los archivos historificados cada 1h
while(1):
	mvDirF = 'mv /home/acerrato/images/*.jpg /home/acerrato/images/f'
	os.system(mvDirF)

	sleep(60)

	rmLocal = 'rm /home/acerrato/images/f/*.jpg.COMPLETED'
	os.system(rmLocal)

	sleep(120)
