import os
import time
import RPIO

def toggle(gpio_id, value):
    os.system("mpc toggle")

RPIO.add_interrupt_callback(4, toggle, edge='rising', pull_up_down=RPIO.PUD_OFF, threaded_callback=False, debounce_timeout_ms=200)






RPIO.wait_for_interrupts(threaded=True)