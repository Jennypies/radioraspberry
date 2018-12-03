import subprocess
from gpiozero import PWMLED
from time import sleep

# set up LED GPIO pins


toggle_led = PWMLED(27)
next_led = PWMLED(13)
prev_led = PWMLED(22)

# LED animations


def led_fade_on():
    toggle_led.pulse(fade_in_time=0.5, fade_out_time=0, n=1, background=True)
    prev_led.pulse(fade_in_time=0.5, fade_out_time=0, n=1, background=True)
    next_led.pulse(fade_in_time=0.5, fade_out_time=0, n=1, background=True)
    sleep(0.4)
    toggle_led.on()
    prev_led.on()
    next_led.on()


def startup_led():
    for _ in range(0, 2):
        toggle_led.pulse(fade_in_time=0.5, fade_out_time=0.5, n=1, background=True)
        sleep(0.1)
        prev_led.pulse(fade_in_time=0.5, fade_out_time=0.5, n=1, background=True)
        sleep(0.1)
        next_led.pulse(fade_in_time=0.5, fade_out_time=0.5, n=1, background=True)
        sleep(1)
        led_fade_on()


def pause_led():
    while b"paused" in subprocess.check_output(["mpc", "status"]):
        toggle_led.pulse(fade_in_time=0.5, fade_out_time=0.5, n=None, background=True)
        next_led.pulse(fade_in_time=0.5, fade_out_time=0.5, n=None, background=True)
        prev_led.pulse(fade_in_time=0.5, fade_out_time=0.5, n=None, background=True)


def led_fade_off():
    toggle_led.pulse(fade_in_time=0, fade_out_time=0.5, n=1, background=True)
    prev_led.pulse(fade_in_time=0, fade_out_time=0.5, n=1, background=True)
    next_led.pulse(fade_in_time=0, fade_out_time=0.5, n=1, background=True)
    sleep(0.4)
    toggle_led.off()
    prev_led.off()
    next_led.off()


def main():
    try:
        # initialise LED start up sequence
        startup_led()
        # While loop for main program
        while True:
            # check mpc status
            if b"paused" in subprocess.check_output(["mpc", "status"]):
                pause_led()
            elif b"play" in subprocess.check_output(["mpc", "status"]):
                led_fade_on
    finally:
        led_fade_off()


if __name__ == "__main__":
    main()
