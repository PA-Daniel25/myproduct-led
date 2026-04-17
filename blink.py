#!/usr/bin/env python3

import gpiod
import time

CHIP = "gpiochip0"
LINE = 16

chip = gpiod.Chip(CHIP)
line = chip.get_line(LINE)

line.request(consumer="blink", type=gpiod.LINE_REQ_DIR_OUT)

try:
    while True:
        line.set_value(1)
        time.sleep(0.5)
        line.set_value(0)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    line.set_value(0)
    line.release()