import serial
import requests
from requests.exceptions import ConnectionError


api="UTX2MK7F8H2H45RD"
def sender(gas):

       if 1:

                payload = {'key': api, 'field2' : str(gas)}
       try :
                r = requests.post("https://api.thingspeak.com/update.json",params=payload)
        #       print r.text
                print "Updated to thingspeak channel"
       except ConnectionError as e:
                print






ser = serial.Serial('/dev/ttyUSB0',9600)


while True:
	
	#ser.write(str(i))
	
	read_serial=ser.readline()

	print read_serial
	
	
       # url = 'http://smartcity.esy.es/waste_bin_script.php'
       # data = dict(air_q = read_serial)
	#r = requests.post(url, data=data, allow_redirects=True)
       # print r.content
      #  print "Updated to database"
	#sender(read_serial)	
	

