#!/usr/bin/python
from sense_hat import SenseHat
import time
import sys
from ISStreamer.Streamer import Streamer
from setting import setting


sense = SenseHat()
logger = Streamer(bucket_name=setting["BUCKET_NAME"], access_key=setting["ACCESS_KEY"])
sense.clear()

try:
    while True:
        temp = sense.get_temperature()
        temp = round(temp, 1)
        logger.log("Temperature C",temp)

        humidity = sense.get_humidity()
        humidity = round(humidity, 1)
        logger.log("Humidity :",humidity)

        pressure = sense.get_pressure()
        pressure = round(pressure, 1)
        logger.log("Pressure:",pressure)

        orientation = sense.get_orientation()
        orientation = "p: {pitch}, r: {roll}, y: {yaw}".format(**orientation)
        logger.log("Orientation:",orientation)


        sense.show_message("Temperature C" + str(temp) + "Humidity:" + str(humidity) + "Pressure:" + str(pressure) + "Orientation:" + str(orientation), scroll_speed=(0.5), back_colour= [0,0,200])

        time.sleep(1)

except KeyboardInterrupt:
    pass

sense.clear()
