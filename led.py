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
            status = subprocess.check_output(["mpc", "status"])
            if b"paused" in status:
                pause_led()
            else:
                led_fade_on()
            subprocess.check_call(["mpc", "idle"])
    finally:
        led_fade_off()


if __name__ == "__main__":
    main()

# subprocess notes- if you want return value use check output, if you just want to send
# a command, use check call
