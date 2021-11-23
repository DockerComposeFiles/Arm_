from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
sleep(2)

i = 0
while i < 10000:
    camera.capture("/pictures/output" + i + ".jpg")
    sleep(60)
exit()
