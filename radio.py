import os
from gpiozero import Button
from signal import pause


toggle_switch = Button(4, pull_up=False)

next_switch = Button(17, pull_up=False, hold_time=0.5, hold_repeat=True,)

previous_switch = Button(27, pull_up=False, hold_time=0.5, hold_repeat=True,)


toggle_switch.when_pressed = os.system("mpc toggle")

next_switch.hold_repeat = os.system("mpc next")

previous_switch.hold_repeat = os.system("mpc prev")

pause()