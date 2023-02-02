import adafruit_bme680
import time
import board
import pandas as pd

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

i = 0

df = pd.DataFrame(columns=['Local Time', 'Unix Time', 'Temperature', 'Gas', 'Humiditiy', 'Pressure', 'Altitude'])

while i < 100:

    info = {'Local Time': time.asctime(time.localtime()),
            'Unix Time': time.time(),
            'Temperature': bme680.temperature,
            'Gas': bme680.gas,
            'Humidity': bme680.relative_humidity,
            'Pressure': bme680.pressure,
            'Altitude': bme680.altitude}
            
    print("\nLocal Time: " + info.get('Local Time'))
    print("Unix Time: ", info.get('Unix Time'))
    print("Temperature: %0.1f C" % info.get('Temperature'))
    print("Gas: %d ohm" % info.get('Gas'))
    print("Humidity: %0.1f %%" % info.get('Humidity'))
    print("Pressure: %0.3f hPa" % info.get('Pressure'))
    print("Altitude = %0.2f meters" % info.get('Altitude'))
    
	df.append(info, ignore_index = True)

	time.sleep(2)

df.to_csv('file_name.csv')
