import os
from time import sleep
from gpiozero import Button
from gpiozero import PWMLED
from signal import pause

toggle_led = PWMLED(27)
next_led = PWMLED(13)
prev_led = PWMLED(22)


def toggle():
    os.system("mpc toggle")


def next_station():
    os.system("mpc next")


def prev_station():
    os.system("mpc prev")


def shutdown():
    shutdown_led()
    os.system("poweroff -h")


def startup_led():
    for _ in range(0, 2):
        toggle_led.pulse(fade_in_time=0.5, fade_out_time=0.5, n=1, background=True)
        sleep(0.1)
        prev_led.pulse(fade_in_time=0.5, fade_out_time=0.5, n=1, background=True)
        sleep(0.1)
        next_led.pulse(fade_in_time=0.5, fade_out_time=0.5, n=1, background=True)
        sleep(1)
    toggle_led.pulse(fade_in_time=0.5, fade_out_time=0, n=1, background=True)
    prev_led.pulse(fade_in_time=0.5, fade_out_time=0, n=1, background=True)
    next_led.pulse(fade_in_time=0.5, fade_out_time=0, n=1, background=True)
    sleep(0.4)
    toggle_led.on()
    prev_led.on()
    next_led.on()


def shutdown_led():
    toggle_led.pulse(fade_in_time=0, fade_out_time=0.5, n=1, background=True)
    prev_led.pulse(fade_in_time=0, fade_out_time=0.5, n=1, background=True)
    next_led.pulse(fade_in_time=0, fade_out_time=0.5, n=1, background=True)
    sleep(0.4)
    toggle_led.off()
    prev_led.off()
    next_led.off()


toggle_switch = Button(4, pull_up=False)
toggle_switch.when_pressed = toggle

next_switch = Button(17, pull_up=False, hold_time=1, hold_repeat=True)
next_switch.when_pressed = next_station
next_switch.when_held = next_station

prev_switch = Button(19, pull_up=False, hold_time=1, hold_repeat=True)
prev_switch.when_pressed = prev_station
prev_switch.when_held = prev_station

shutdown_switch = Button(3, pull_up=True, hold_time=3, hold_repeat=False)
shutdown_switch.when_held = shutdown


def main():
    startup_led()
    try:
        pause()
    finally:
        shutdown_led()


if __name__ == "__main__":
    main()
