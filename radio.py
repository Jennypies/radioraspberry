import os
from gppiozero import Button
from signal import pause

toggle_switch = Button(4, *, pull_up=False, bounce_time=200, hold_time=2, hold_repeat=True, pin_factory=None)

def toggle()):
    os.system("mpc toggle")

toggle_switch.when_pressed = toggle

pause()