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

while (time.time() - start_time < runtime * 60):
    if ((time.time() - start_time)%60 < 0.5):
        cpm.append(count)
        print("There were {:} counts in the last minute.".format(count))
        count = 0
    if GPIO.event_detected(pin_num):
        count += 1
        time_stamps.append(time.time())
        print("Count at time: {:}".format(time_stamps[-1]))

print("Over the span of {} minutes, we measured {:} counts.".format(runtime_minutes, len(detected_times)))
