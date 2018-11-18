import os
from gpiozero import Button
from signal import pause


toggle_switch = Button(4, pull_up=False, bounce_time=100, hold_time=1, hold_repeat=False, pin_factory=None)

def toggle():
    os.system("mpc toggle")

    toggle_switch.when_pressed = toggle

pause()