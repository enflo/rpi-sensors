# raspberry pi weather station

## Equipment

    Raspberry Pi 2 or 3
    Micro SD Card or a SD card if you’re using an old version of the Pi.
    Power Supply
    Sense HAT
    Ethernet Cable or WiFi Dongle (The Pi 3 has WiFi inbuilt)

    Optional:
        Raspberry Pi Case

## Getting started

### Prepare Raspberry PI

```
sudo apt-get update
sudo apt-get upgrade
```

### Install SenseHat and Twython python module

```
pip3 install sense-hat
pip3 install Twython
```

### Clone repository

```
git clone https://github.com/enflo/rpi-weather-station-sense-pi-hat.git /home/pi
```

## Install  InitialState

Before we get started with implementing everything for the Raspberry Pi weather station, we will first have to sign up for a free account over at their website https://www.initialstate.com/.

You need registre into intialstate and generate a key and a bucket name

### Installing InitialState python streamer

```
curl -ssl https://get.initialstate.com/python -o - | sudo bash
```

press N to skip having to download the example code, and we will not need it for our tutorial.

### Edit setting.py

Change values:

```
    BUCKET_NAME = "you bucket name"
    ACCESS_KEY = "you access tocken"
```

## Create start script at startup

Before we get started with setting up our script, we first need to install an additional package we may have to rely on. This package is dos2unix, and this converts DOS-style line endings into something that is Unix friendly.
```
sudo apt-get install dos2unix
```

Execute this command for copy  service script into /etc/init.d/

```
cp /home/pi/rpi-weather-station-sense-pi-hat/weatherstation_service.sh /etc/init.d/weatherstation
```

```
sudo dos2unix /etc/init.d/weatherstation
```

```
sudo chmod 755 /home/pi/rpi-weather-station-sense-pi-hat/weather_script.py
```

```
sudo chmod +x /etc/init.d/weatherstation
```

We need to create a symbolic link between our bash script and the rc.d folders. We can do that by running the following command in terminal.
```
sudo update-rc.d weatherstation defaults
```

To start up our Python script, we can just run the following command.
```
sudo service weatherstation start
```

The last command shown below retrieves the status of the weatherstation service and our weather_script.py script

```
sudo service weatherstation status
```
