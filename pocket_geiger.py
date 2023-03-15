import RPi.GPIO as GPIO
import time

start_time = time.time()
runtime_minutes = 5

pin_num = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_num, GPIO.IN)
GPIO.add_event_detect(pin_num, GPIO.FALLING)


cpm = []
time_stamps = []
count = 0
last_run = 0

while ((time.time() - start_time) < runtime_minutes * 60):
    if ((time.time() - start_time)%60 < last_run):
        cpm.append(count)
        print("There were {:} counts in the last minute.".format(count))
        count = 0
    last_run = (time.time() - start_time)%60
    print(GPIO.event_detected(pin_num))
    if GPIO.event_detected(pin_num):
        count += 1
        time_stamps.append(time.time())
        print("Count at time: {:}".format(time_stamps[-1]))
        
if(len(cpm) != runtime_minutes):
    cpm.append(count)
    
print("Over the span of {} minutes, we measured {:} counts.".format(runtime_minutes, len(time_stamps)))
