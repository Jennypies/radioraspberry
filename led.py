import subprocess
from gpiozero import LED
from time import sleep

# set up LED GPIO pins


toggle_led = LED(27)
next_led = LED(13)
prev_led = LED(22)


def startup_led():
    for x in range(2):
        toggle_led.on()
        next_led.on()
        prev_led.on()
        sleep(1)
        toggle_led.off()
        next_led.off()
        prev_led.off()
        sleep(1)
    toggle_led.on()
    next_led.on()
    prev_led.on()


def pause_led():
        toggle_led.on()
        next_led.on()
        prev_led.on()
        sleep(1)
        toggle_led.off()
        next_led.off()
        prev_led.off()
        sleep(1)


def led_fade_off():
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
                toggle_led.on()
                next_led.on()
                prev_led.on()
            subprocess.check_call(["mpc", "idle"])
    finally:
        led_fade_off()


if __name__ == "__main__":
    main()

# subprocess notes- if you want return value use check output, if you just want to send
# a command, use check call
