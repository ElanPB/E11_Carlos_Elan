import adafruit_bme680
import time
import board

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

i = 0

file = open('CSV_FILES/' + time.strftime("%Y%m%d-%H%M%S", time.localtime()) + '.csv', 'w')
data = []
header = ['Local Time', 'Unix Time', 'Temperature', 'Gas', 'Humidity', 'Pressure', 'Altitude']

while i < 100:

    info = [time.asctime(time.localtime()), time.time(), bme680.temperature,\
        bme680.gas, bme680.relative_humidity, bme680.pressure, bme680.altitude]
            
    print("\nLocal Time: " + info[0])
    print("Unix Time: ", info[1])
    print("Temperature: %0.1f C" % info[2])
    print("Gas: %d ohm" % info[3])
    print("Humidity: %0.1f %%" % info[4])
    print("Pressure: %0.3f hPa" % info[5])
    print("Altitude = %0.2f meters" % info[6])
    
    data.append(info)
    
    time.sleep(2)
    
    i += 1

file.write(','.join(header) + ',\n')
for i in data:
    line = ''
    for x in i:
        line += str(x) + ','
    file.write(line + '\n')
file.close()