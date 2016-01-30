import RPi.GPIO as GPIO
import time
import Adafruit_DHT
from mechanize import Browser

br = Browser()

sensor = Adafruit_DHT.DHT11
GPIO.setmode(GPIO.BOARD)

pin = 4

n = 0
x = 5

while x>0:
	print n
	x = x - 1
	Humidity , Temperature = Adafruit_DHT.read_retry(sensor, pin) 
	n = n + 1
	print str(Humidity) + "%"
	print str(Temperature) + " C"

	if Humidity == None or Temperature == None:
		continue

	f1 = open('temp', 'w')
	f2 = open('humi', 'w')
	f1.write(str(Temperature))
	f2.write(str(Humidity))
	f1.close()
	f2.close()
	GPIO.setup(11, GPIO.OUT) 

	if Temperature >= 27:
		GPIO.output(11, GPIO.LOW)
	elif Temperature < 27:
		GPIO.output(11, GPIO.HIGH)

	
	br.open('http://140.112.30.53:8787/mouse13/temptxt')
	br.select_form('upload')
	br.form.add_file(open('./temp', 'rb'), 'text/plain', 'temp')
	br.submit()
	br.open('http://140.112.30.53:8787/mouse13/humitxt')
	br.select_form('upload')
	br.form.add_file(open('./humi', 'rb'), 'text/plain', 'humi')
	br.submit()
	
	if n > 100:
		break
	time.sleep(5)

GPIO.output(11, GPIO.LOW)
GPIO.cleanup()
