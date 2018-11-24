import os
from time import sleep
from gpiozero import Button
from gpiozero import PWMLED
from signal import pause

toggle_switch = Button(4, pull_up=False)

def toggle(): 
    os.system("mpc toggle")

next_switch = Button(17, pull_up=False, hold_time=1, hold_repeat=True,)

def next_station():
    os.system("mpc next")

prev_switch = Button(19, pull_up=False, hold_time=1, hold_repeat=True,)

def prev_station():
    os.system("mpc prev")

shutdown_switch = Button(3, pull_up=True, hold_time=3, hold_repeat=False)

prev_led = PWMLED(22)
next_led = PWMLED(13)
toggle_led = PWMLED(27)

def startup_led():
    for _ in range(0, 3):
        toggle_led.pulse(fade_in_time=0.5, fade_out_time=0.5, n=1, background=True)
        sleep(0.1)
        prev_led.pulse(fade_in_time=0.5, fade_out_time=0.5, n=1, background=True)
        sleep(0.1)
        next_led.pulse(fade_in_time=0.5, fade_out_time=0.5, n=1, background=True)
        sleep(0.8)


def shutdown_led():
    pass


def shutdown():
    shutdown_led()
    os.system("poweroff -h")




toggle_switch.when_pressed = toggle
next_switch.when_pressed = next_station
next_switch.when_held = next_station

prev_switch.when_pressed = prev_station
prev_switch.when_held = prev_station

shutdown_switch.when_held = shutdown


startup_led()

try:
    pause()
finally:
    shutdown_led()