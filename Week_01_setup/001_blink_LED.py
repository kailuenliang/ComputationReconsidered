import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# this is a variable, a name for the variable and the assignment, you can use = to assign a value
counter = 0

while True:
    led.value = True
    print("how many times the counter has blinked: ", counter)

    # this is a comment, the code editor will not run this code
    # this is another comment

    counter+=1
    time.sleep(1.0)
    led.value = False
    time.sleep(1.0)
