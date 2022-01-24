
# documentation:
# https://circuitpython.readthedocs.io/en/latest/shared-bindings/touchio/index.html


import board
import touchio

#define pins
touch_pin_01 = touchio.TouchIn(board.A1)

while True:

    print(touch_pin_01.value)
