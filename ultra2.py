import RPi.GPIO as GPIO 
import time
import requests
from requests.exceptions import ConnectionError
 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

TRIG = 23 
ECHO = 24 
LED = 25
#time.sleep(60)

api="UTX2MK7F8H2H45RD"
def sender(trash_no,level):

       if trash_no == 1:
		
                payload = {'key': api, 'field1' : str(level), 'field2': str(55)}
       try :
       		r = requests.post("https://api.thingspeak.com/update.json",params=payload)
      		print r.text
       except ConnectionError as e:   
   		print 
   		


print "Distance Measurement In Progress" 
GPIO.setup(TRIG,GPIO.OUT) 
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED, False)
while True : 
	
	GPIO.output(TRIG, False) 
	print "Waiting For Sensor To Settle" 
	time.sleep(2) 
	GPIO.output(TRIG, True) 
	time.sleep(0.00001) 
	GPIO.output(TRIG, False) 
	while GPIO.input(ECHO)==0:
  		pulse_start = time.time() 
	while GPIO.input(ECHO)==1:
  		pulse_end = time.time() 
	pulse_duration = pulse_end - pulse_start 
	level = pulse_duration * 17150
	#print level 
	level = (100 -( (level / 19.5 )* 100)) 
	level = round(level, 2)
	if level < 5 :
		level = 0
	if level > 60 :
		GPIO.output(LED, True)
	else:
		GPIO.output(LED, False)
 
	print "Level:",level,"  %"
	sender(1,level)
	time.sleep(13) 
GPIO.cleanup()
