import os
from gpiozero import Button


toggle_switch = Button(4, pull_up=False, bounce_time=200, hold_time=300, hold_repeat=True, pin_factory=None)

def toggle():
    os.system("mpc toggle")

while True:
    toggle_switch.when_pressed = toggle

