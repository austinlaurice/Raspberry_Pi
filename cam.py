import picamera
import time
from mechanize import Browser

br = Browser()

with picamera.PiCamera() as camera:
	camera.start_preview()
	camera.resolution = (320, 240)
	a = 100
	while a>0:
		name = 'mouse' + str(a) + '.jpg'
		print str(100-(a-1)) + 'th photo ' + 'took'
		time.sleep(60)
		camera.capture(name)
		br.open('http://140.112.30.53:8787/mouse13/upload')
		br.select_form('upload')
		br.form.add_file(open(name, 'rb'), 'text/plain', name)
		br.submit()
		a = a - 1
