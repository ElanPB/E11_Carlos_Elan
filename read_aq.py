import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C

reset_pin = None
#reset_pin = DigitalInOut(board.G0)
#reset_pin.direction = Direction.OUTPUT
#reset_pin.value = False


#Using Raspberry Pi
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

print("Found PM2.5 sensor, reading data...")

file = open(time.strftime("%Y%m%d_%H:%M:%S", time.localtime()) + '.csv', 'w')
data = []
header = ['Local Time', 'Unix Time', 'PM1.0', 'PM2.5', 'PM10']

i = 0
while (i < 30):
    time.sleep(1)

    try:
        aqdata = pm25.read()
        # print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue

    info = [time.asctime(time.localtime()), time.time(), aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"]]

    print()
    print("Concentration Units (standard)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (info[0], info[1], info[2])
    )
    print("Concentration Units (environmental)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
    )
    print("---------------------------------------")
    print("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
    print("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
    print("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
    print("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
    print("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
    print("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])
    print("---------------------------------------")

    data.append(info)

    i += 1

file.write(','.join(header) + ',\n')
for i in data:
    file.write(','.join(i) + ',\n')
file.close()