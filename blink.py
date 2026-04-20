#!/usr/bin/env python3

import time
import gpiod
from gpiod.line import Direction, Value

CHIP = "/dev/gpiochip0"
LINE = 16

req = gpiod.request_lines(
    CHIP,
    consumer="myproduct-led",
    config={
        LINE: gpiod.LineSettings(direction=Direction.OUTPUT)
    },
    output_values={LINE: Value.INACTIVE},
)

try:
    while True:
        req.set_value(LINE, Value.ACTIVE)
        time.sleep(0.5)
        req.set_value(LINE, Value.INACTIVE)
        time.sleep(0.5)
finally:
    req.set_value(LINE, Value.INACTIVE)
    req.release()