import RPi.GPIO as GPIO
import time

start_time = time.time()
runtime = 5 * 60 #s
cpm = []
time_stamps = []
count = 0

GPIO.setmode(GPIO.BCM)
pin_num = 23

def my_callback(pin_num):
    global time_stamps
    time_stamps.append(time.time())
    global count
    count += 1
    print("Event detected at" + str(time.time()))

GPIO.setup(pin_num, GPIO.IN)
GPIO.add_event_detect(pin_num, GPIO.FALLING, callback = my_callback(pin_num))

while ((time.time() - start_time) < runtime):
    time.sleep(60)
    cpm.append(count)
    count = 0

print("Over the span of %d seconds, we measured %d counts." %(runtime, len(time_stamps)))