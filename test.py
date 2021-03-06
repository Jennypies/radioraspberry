import subprocess
from time import sleep
from gpiozero import PWMLED

toggle_led = PWMLED(27)
next_led = PWMLED(13)
prev_led = PWMLED(22)

while True:
    # update staus LEDs
    if b"paused" in subprocess.check_output(["mpc", "status"]):
        toggle_led.pulse(fade_in_time=0.5, fade_out_time=0.5, n=None, background=True)
        next_led.pulse(fade_in_time=0.5, fade_out_time=0.5, n=None, background=True)
        prev_led.pulse(fade_in_time=0.5, fade_out_time=0.5, n=None, background=True)
    else:
        toggle_led.pulse(fade_in_time=0.5, fade_out_time=0, n=1, background=True)
        next_led.pulse(fade_in_time=0.5, fade_out_time=0, n=1, background=True)
        prev_led.pulse(fade_in_time=0.5, fade_out_time=0, n=1, background=True)
        sleep(0.4)
        toggle_led.on()
        prev_led.on()
        next_led.on()
    # wait for status to change
    subprocess.check_output(["mpc", "idle"])
