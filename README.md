# DHT22-to-1-Wire-Format
#### Converts DHT22 to 1-Wire output for use with Openauto Pro

This script allows a DHT22 Temperature/Humidity sensor to be used in OpenAuto Pro with the existing 1-wire support.  The format of these sensors are different, so this will convert the values that come from those into a format that works for their integration.  The default path to the sensor is set up for the driver at https://github.com/KermsGit/dht22 but could be changed to work with whatever you are using.

### How to use

- Clone repo and cd into it
- Run ```./convert_temp.py``` once manually to create the needed directory and file
- Verify that running ```cat /home/pi/.openauto/temp_conversion/convert_temp.py``` shows output like the following
```
# cat ../.openauto/temp_conversion/temp.txt 
31 00 4b 46 ff ff 05 10 1c : crc=1c YES
31 00 4b 46 ff ff 05 10 1c t=24000.0
```
- Copy convert_temp.py to /home/pi/.openauto/temp_conversion/
- Copy convert_temp.service to /etc/systemd/system/convert_temp.service
- Run ```systemctl systemctl daemon-reload```
- Run ```systemctl enable --now convert_temp```
- Verify that it is running properly
```
# ps faux | grep convert_temp.py
root      2133  0.0  0.0   7348   532 pts/0    S+   01:12   0:00                          \_ grep convert_temp.py
root      2019  0.2  0.9  14424  7272 tty3     Ss+  01:11   0:00 /usr/bin/python3 /home/pi/.openauto/temp_conversion/convert_temp.py
```
- Set the ```TemperatureSensorDescriptor``` option in ```/home/pi/.openauto/config/openauto_system.ini``` to the temp.txt file path
```
TemperatureSensorDescriptor=/home/pi/.openauto/temp_conversion/temp.txt
```
- Reboot
- Verify that temperature is showing correctly on the OpenAuto interface