import os
from gpiozero import Button
from signal import pause

toggle_switch = Button(4, pull_up=False)

def toggle(): 
    os.system("mpc toggle")

next_switch = Button(17, pull_up=False, hold_time=1, hold_repeat=True,)

def next_station():
    os.system("mpc next")

prev_switch = Button(27, pull_up=False, hold_time=1, hold_repeat=True,)

def prev_station():
    os.system("mpc prev")

shutdown_switch = Button(22, pull_up=False,)

def shutdown():
    os.system("poweroff -h")



toggle_switch.when_pressed = toggle

next_switch.when_pressed = next_station
next_switch.when_held = next_station

prev_switch.when_pressed = prev_station
prev_switch.when_held = prev_station

shutdown_switch.when_held = shutdown

pause()