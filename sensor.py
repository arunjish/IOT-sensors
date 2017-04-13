#! /usr/bin/python

import requests
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(4, GPIO.BOTH)
GPIO.add_event_detect(18,GPIO.BOTH)


api="6PRGMZEQ52GWF3E1"
def sender(sensor_no,sensor_value):

       if sensor_no == 4:		  	

       		payload = {'key': api, 'field1' : str(sensor_value)}
       if sensor_no == 18:
		payload = {'key': api, 'field2' : str(sensor_value)}
       r = requests.post("https://api.thingspeak.com/update.json",params=payload)
       print r.text
      

def my_callback(self):
	if GPIO.input(self):
		print 'sensor at'+str(self)+ ' on !!'
		sender(self,5)
	else:
		print 'sensor at'+str(self)+' off !!'
		sender(self,0)


GPIO.add_event_callback(4,my_callback)
GPIO.add_event_callback(18,my_callback)
while True:
	k=1		
