import subprocess
from gpiozero import LED
from time import sleep

# set up LED GPIO pins


toggle_led = LED(27)
next_led = LED(13)
prev_led = LED(22)


def main():
    try:
        # While loop for main program
        while True:
            toggle_led.on()
            next_led.on()
            prev_led.on()
            sleep(1)
            # check mpc status
            status = subprocess.check_output(["mpc", "status"])
            if b"paused" in status:
                toggle_led.off()
                prev_led.off()
                next_led.off()
                sleep(1)
    finally:
        toggle_led.off()
        prev_led.off()
        next_led.off()


if __name__ == "__main__":
    main()

# subprocess notes- if you want return value use check output, if you just want to send
# a command, use check call
