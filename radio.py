import os
from gpiozero import Button
from signal import pause


toggle_switch = Button(4, pull_up=False)
def toggle(): 
    os.system("mpc toggle")

next_switch = Button(17, pull_up=False, hold_time=0.5, hold_repeat=True,)
def next_station():
    os.system("mpc next")

previous_switch = Button(27, pull_up=False, hold_time=0.5, hold_repeat=True,)
def prev_station():
    os.system("mpc prev")

toggle_switch.when_pressed = toggle

next_switch.hold_repeat = next_station

previous_switch.hold_repeat = prev_station

pause()