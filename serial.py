import threading

from serial import serial
import socket

lastcommand = ''

ser = serial.Serial('/dev/ttyUSB0', 9600)

    
   
command='STRAIGHT'
  
ser.write(command)
       
