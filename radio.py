import os
from gpiozero import Button
from signal import pause


toggle_switch = Button(4, pull_up=False, hold_time=0.5, hold_repeat=True)

def toggle():
    os.system("mpc toggle")



#toggle_switch.when_pressed = toggle
toggle_switch.when_held = toggle

pause()