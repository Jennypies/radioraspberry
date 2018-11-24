import os
from time import sleep
from gpiozero import Button
from gpiozero import LED
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

def shutdown():
    toggle_led.off()
    prev_led.off()
    next_led.off()
    os.system("poweroff -h")

prev_led = LED(22)
next_led = LED(13)
toggle_led = LED(27)

def startup():
    for x in range (0, 1):
        toggle_led.on()
        sleep(0.3)
        toggle_led.off()
        prev_led.on()
        sleep(0.3)
        prev_led.off()
        next_led.on()
        sleep(0.3)
        next_led.off()
        sleep(0.6)
    toggle_led.on()
    prev_led.on()
    next_led.on()

toggle_switch.when_pressed = toggle
next_switch.when_pressed = next_station
next_switch.when_held = next_station

prev_switch.when_pressed = prev_station
prev_switch.when_held = prev_station

shutdown_switch.when_held = shutdown


startup()
pause()