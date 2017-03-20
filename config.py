
#if u r using temprature sensor please provide chanel number(0-7)
tmpchanelpin1 = 0
tmpchanelpin2 = 0
tmpspiclk = 16 #clock pin of IC to be connected to RPi
tmpspimiso = 20 #output of the IC to input to the RPi
tmpspimosi = 21 #input to the IC to the output of the RPi
tmpcs = 25 #chip select of IC
UserName = "mahendra.bilagi@gmail.com" #your user name used in developer.paasmer.co for registration
DeviceName = "HariPi" #your device name
feedname1 = "TemprSensor" #feed name used for displaying in the developer.paasmer.co This feed is restricted to temprature sensor
feedtype1 = " " # type should be in ['temp','digital'] for Temprature sensor we have buld a functionality fo fetch temprature directly
sensorpin1 = 4 #gpio-pin-no-for-sensor-1 modify with the pin number which you connected the sensor, eg 6 or 7 or 22
feedname2 = "Soil moisture sensor" #feed name used for display in the developer.paasmer.co this feed is restricted to digital sensor
feedtype2 = "digital" # type should be in ['temp','digital']
sensorpin2 = 12 #gpio-pin-no-for-sensor-2 modify with the pin number which you connected the sensor, eg 6 or 7 or 22
feedname3 = "" #feed name used for display in the developer.paasmer.co this feed is restricted to digital sensor
feedtype3 = "" # type should be in ['temp','digital'] for Temprature sensor we have buld a functionality fo fetch temprature directly
sensorpin3 = 16 #gpio-pin-no-for-sensor-3 modify with the pin number which you connected the sensor, eg 6 or 7 or 22
feedname4 = "Water level sensor" #feed name used for displaying in the developer.paasmer.co, This Feed is restricted to Distance sensor(Ultrasonic)
feedtype4 = "distance" #Please do not edit this line
distancepin1 = 23 #modyfy your pin number, our Python SDK works with RPi.BCM mode
distancepin2 = 24 #modyfy your pin number, our Python SDK works with RPi.BCM mode
controlfeedname1 = "sprinkler" #feed name used for display in the developer.paasmer.co
controlpin1 = 17 #modify with the pin number which you connected the control device (eg.: motor)
controlfeedname2 = "water_motor" #feed name used for display in the developer.paasmer.co
controlpin2 = 5 #modify with the pin number which you connected the control device (eg.: fan)
timePeriod = 5 #change the time delay(in seconds) as you required for sending sensor values to paasmer cloud
