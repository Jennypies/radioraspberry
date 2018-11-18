import os
from gpiozero import Button
from signal import pause


toggle_switch = Button(4, pull_up=False, bounce_time=1)

def toggle():
    os.system("mpc toggle")



toggle_switch.when_pressed = toggle

pause()