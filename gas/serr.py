import serial

import socket

import time





ser = serial.Serial('/dev/ttyUSB0', 9600)



command='S'

print(command)

    

ser.write(command)
while True:
	command=ser.readline()
	time.sleep(3)
	command='S'
	ser.write(command)
		
	print command
       
