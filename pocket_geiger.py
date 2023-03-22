import RPi.GPIO as GPIO
import time

file = open('CSV_FILES/' + time.strftime("%Y%m%d-%H%M%S", time.localtime()) + '_pocket_geiger.csv', 'w')
file.write('Time Stamps\n')

start_time = time.time()
runtime = 2 * 60 #s
cpm = []
time_stamps = []
count = 0

GPIO.setmode(GPIO.BCM)
pin_num = 6

def my_callback(pin_num):
    global time_stamps, count
    time_stamps.append(time.time())
    count += 1
    print("Event detected at " + str(time.time()))

GPIO.setup(pin_num, GPIO.IN)
GPIO.add_event_detect(pin_num, GPIO.FALLING, callback = my_callback)

while ((time.time() - start_time) < runtime):
    time.sleep(10)
    cpm.append(count)
    count = 0

for i in cpm:
    file.write(str(i) + '\n')

file.close()

print("Over the span of %d seconds, we measured %d counts." %(runtime, len(time_stamps)))