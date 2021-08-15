#!/usr/bin/env python

import time
import os

temp_file = '/sys/devices/platform/dht22@0/iio:device0/in_temp_input'
dir_path = '/home/pi/.openauto/temp_conversion'
write_file = '/home/pi/.openauto/temp_conversion/temp.txt'

def check_path():
    ''' Verify that the paths exist '''
    if os.path.isdir(dir_path):
        return True
    else:
        os.mkdir(dir_path)

    if os.path.isfile(write_file):
        return True
    else:
        create_file = open(write_file, 'w')
        create_file.close()



def convert_temp():
    while True:
        file = open(temp_file, 'r').read()
        writefile = open(write_file, 'w')
        converted_temp = float(file) * 1000
        writefile.write('31 00 4b 46 ff ff 05 10 1c : crc=1c YES\n31 00 4b 46 ff ff 05 10 1c t=' + str(converted_temp))
        writefile.close()
        time.sleep(10)

def main():
    check_path()
    convert_temp()

if __name__ == '__main__':
    main()
