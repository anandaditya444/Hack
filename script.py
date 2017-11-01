import time
import commands
import numpy as np
import cv2

#integrated webacm on my PC
camera_port = -1
#Set up the camera
camera = cv2.VideoCapture(camera_port)

def get_image():
    "return full image out of a capture object"
    retval, image = camera.read()
    return image

while True:
    image = get_image()
    x = 1.0 - round((np.mean(image)/256.0) * 1,2)
    #using /sys/class/backlight to change brightness file value - Hack
    #cmd = ("sudo su -c 'echo " + str(x) + " > /sys/class/backlight/acpi_video0/brightness'")
    #using xrandr using to change brightness - Tool
    cmd = (" xrandr --output VGA-1  --brightness " + str(x))
    status, output = commands.getstatusoutput(cmd)
    assert status is 0
    time.sleep(10)
