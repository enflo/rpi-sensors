#!/usr/bin/python
import Adafruit_DHT
import time
import datetime
import requests
import json

from influxdb import InfluxDBClient

DHT_SENSOR = Adafruit_DHT.AM2302
DHT_PIN = 4

DEVICE = ["Raspberry Pi 3+", "DHT22"]
USERNAME = "Antoni Florit Homar"
URL = "https://weather.toniflorithomar.dev/ambient/"
INFLUXURL = "https://influx.toniflorithomar.dev/write?db=weather"
CITY_NAME = "Palma"
LONGIUDE = "2.67788529"
LATITUDE = "39.58578071"
SEALEVEL = "27 m"

client = InfluxDBClient(host='influx.toniflorithomar.dev', ssl=True, verify_ssl=True)
client.switch_database('weather')

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        temp = temperature
        if temp:
            temp = round(temp, 1)
        else:
            hum = ""
        print("Temperature C",temp)

        hum = humidity
        if hum:
            hum = round(hum, 1)
        else:
            hum = ""
        print("Humidity :",hum)

        pressure = "none"
        #pressure = round(pressure, 1)
        #logger.log("Pressure:",pressure)

        payload = {
                      "username": USERNAME,
                      "city": {
                        "name": CITY_NAME,
                        "longitude": LONGIUDE,
                        "latitude": LATITUDE,
                        "sealevel": SEALEVEL
                      },
                      "datetime": str(datetime.datetime.now()),
                      "devices": DEVICE,
                      "temperature": str(temp),
                      "humidity": str(hum),
                      "pressure": str(pressure)
                    }

        headers = {
                    "Content-Type": "application/json"
                    }
        print(payload)
        response = requests.request("POST", URL, headers=headers, data=json.dumps(payload))
        print(response)

        now_ns = int(round(time.time() * 1000000000))
        influx_string = f"ambient,username={USERNAME},city_name={CITY_NAME},temperature={temp},humidity={hum},pressure={pressure} value=0.64 {now_ns}"
        response = requests.request("POST", INFLUXURL, data=influx_string)
        time.sleep(300)

except KeyboardInterrupt:
    pass
