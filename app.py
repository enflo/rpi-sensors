#!/usr/bin/python
import Adafruit_DHT
import time
import datetime
import requests

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 3

DEVICE = ["Raspberry Pi 3+", "DHT22"]
USERNAME = "Antoni Florit Homar"
URL= "https://weather.toniflorithomar.dev/ambient/"
CITY_NAME = "Palma"
ALTITUDE = ""
LATITUDE = ""
SEALEVEL = ""

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        temp = temperature
        temp = round(temp, 1)
        print("Temperature C",temp)

        hum = humidity
        hum = round(hum, 1)
        print("Humidity :",hum)

        pressure = "none"
        #pressure = round(pressure, 1)
        #logger.log("Pressure:",pressure)

        payload = {
                      'username': USERNAME,
                      'city': {
                        'name': CITY_NAME,
                        'longitude': ALTITUDE,
                        'latitude': LATITUDE,
                        'sealevel': SEALEVEL
                      },
                      'datetime': str(datetime.datetime.now()),
                      'devices': DEVICE,
                      "temperature": temp,
                      "humidity": hum,
                      "pressure": pressure
                    }

        headers = {
                    'Content-Type': 'application/json'
                    }

        response = requests.request("POST", URL, headers=headers, data=payload

        time.sleep(300)

except KeyboardInterrupt:
    pass
