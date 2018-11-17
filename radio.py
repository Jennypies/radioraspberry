import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(4, GPIO.RISING)

def toggle_callback():
    os.system("mpc toggle")

GPIO.add_event_callback(4, toggle_callback)
time.sleep(9999)