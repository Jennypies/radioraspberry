import subprocess
from gpiozero import Button
from signal import pause


def toggle():
    subprocess.check_call(["mpc", "toggle"])


def next_station():
    subprocess.check_call(["mpc", "next"])


def prev_station():
    subprocess.check_call(["mpc", "prev"])


def shutdown():
    subprocess.check_call(["poweroff", "-h"])


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
    pause()


if __name__ == "__main__":
    main()
