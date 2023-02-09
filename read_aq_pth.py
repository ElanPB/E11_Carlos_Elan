import time #AQ, PTH
import board #AQ, PTH
import busio #AQ
import adafruit_bme680 #PTH
from digitalio import DigitalInOut, Direction, Pull #AQ
from adafruit_pm25.i2c import PM25_I2C #AQ

#AQ sensor input
reset_pin = None

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

#PTH sensor input
i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

runtime = 30 #seconds

file = open('CSV_FILES/' + time.strftime("%Y%m%d_%H:%M:%S", time.localtime()) + '_aq_pth.csv', 'w')
header = ['Local Time', 'Unix Time', 'PM1.0', 'PM2.5', 'PM10', \
    'Temperature', 'Gas', 'Humidity', 'Pressure', 'Altitude']
data = []

i = 0
while (i < runtime):
    try:
         aqdata = pm25.read()
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue

    info = [time.asctime(time.localtime()), time.time(), \
        aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"], \
        bme680.temperature, bme680.gas, bme680.relative_humidity, bme680.pressure, bme680.altitude]

    #Print AQ and PTH sensor outputs here

    data.append(info)

    time.sleep(1)
    i += 1

file.write(','.join(header) + ',\n')
for i in data:
    line = ''
    for x in i:
        line += str(x) + ','
    file.write(line + '\n')
file.close()