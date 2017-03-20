# SBC-SDK-PYTHON
**Paasmer IoT SDK - Python** for Single Board Computers Running Linux

## Overview

The **Paasmer SDK - Python** for **Single Board Computers (SBC)** like Raspberry-PI, Intel Edison, Beagle Bone is a collection of source files that enables you to connect to the Paasmer IoT Platform. It includes the trasnport client for **MQTT** with **TLS** support.  It is distributed in source form and intended to be built into customer firmware along with application code, other libraries and RTOS.

## Featuers

The **SBC-SDK-PYTHON** simplifies access to the Pub/Sub functionality of the **Paasmer IoT** broker via **MQTT**. **The SDK has been tested to work on the Raspberrp Pi 3 running Raspbian Jessie**. Support for Other SBC's running any flavors of Linux would be available shortly.

## MQTT Connection

The **SBC-SDK-PYTHON** provides functionality to create and maintain a mutually authenticated TLS connection over which it runs **MQTT**. This connection is used for any further publish operations and allow for subscribing to **MQTT** topics which will call a configurable callback function when these topics are received.

## Pre Requisites

Registration on the portal http://developers.paasmer.co, is necessary to connect the devices to the **Paasmer IoT Platfrom** .The SDK has been tested on the Raspberry PI 3 with Raspbian Jessie (https://downloads.raspberrypi.org/raspbian_latest). Python 2.7 needs to be pre installed on the Raspberry PI 3. 

# Installation

* Download the SDK or clone it using the command below.
```
$ git clone https://github.com/Paasmer/SBC-SDK-PYTHON
$ cd SBC-SDK-PYTHON
```

* To connect the device to Paasmer IoT Platfrom, the following steps need to be performed.

```
$ cd /paasmer-iot-device-sdk-python/
$ sudo ./install.sh
```

* Upon successful completion of the above command, the following commands need to be executed.
```
$ sudo su
$ source ~/.bashrc
$ PAASMER
$ sed -i 's/alias PAASMER/#alias PAASMER/g' ~/.bashrc
$ exit
```


* Edit the config.h file to include the user name(Email), device name, feed names and GPIO pin details.
```c

#if u r using temprature sensor please provide chanel number(0-7)
tmpchanelpin1 = 0
tmpchanelpin2 = 0
tmpspiclk = 16
#clock pin of IC to be connected to RPi
tmpspimiso = 20 
#output of the IC to input to the RPi
tmpspimosi = 21 
#input to the IC to the output of the RPi
tmpcs = 25 
#chip select of IC
UserName = "XXXXYYYY@gmail.com" 
#your user name used in developer.paasmer.co for registration
DeviceName = "RASPi" 
#your device name
feedname1 = "TemprSensor" 
#feed name used for displaying in the developer.paasmer.co This feed is restricted to temprature sensor
feedtype1 = " " 
# type should be in ['temp','digital'] for Temprature sensor we have buld a functionality fo fetch temprature directly
sensorpin1 = 4 
#gpio-pin-no-for-sensor-1 modify with the pin number which you connected the sensor, eg 6 or 7 or 22
feedname2 = "Soil moisture sensor" 
#feed name used for display in the developer.paasmer.co this feed is restricted to digital sensor
feedtype2 = "digital" 
# type should be in ['temp','digital']
sensorpin2 = 12 
#gpio-pin-no-for-sensor-2 modify with the pin number which you connected the sensor, eg 6 or 7 or 22
```

* Go to the diectory below.
```
$ cd samples/basicPubSub/
```
      
* Run the code using the command below.
```
$ sudo python basicPubSub.py
```

* The device would now be connected to the Paasmer IoT Platfrom and publishing sensor values are specified intervals.

## Support

The support forum is hosted on the GitHub, issues can be identified by users and the Team from Paasmer would be taking up requests and resolving them. You could also send a mail to support@paasmer.co with the issue details for quick resolution.

## Note

* The Paasmer IoT SBC-SDK-PYTHON utilizes the features provided by AWS-IOT-SDK for Python.
