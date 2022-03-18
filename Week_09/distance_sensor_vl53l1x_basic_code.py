# Write your code here :-)

# code for Time of Flight Distance Sensor
# more info tutorial here:
# https://www.youtube.com/watch?v=7KookmtWQSg&list=PL9VJ9OpT-IPSsQUWqQcNrVJqy4LhBjPX2&index=13

import board, time, adafruit_vl53l1x

i2c = board.I2C()
distance_sensor = adafruit_vl53l1x.VL53l1X(i2c)

# start the distance sensor
distance_sensor.start_ranging()


while True:
    if distance_sensor.data_ready:
        distance = distance_sensor.distance
        print("Distance: {0} cm, {1:.2f} in".format(distance, distance * 0.394))
        distance_sensor.clear_interrupt()
        time.sleep(0.1)
