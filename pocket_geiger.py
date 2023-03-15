import RPi.GPIO as GPIO
import time

start_time = time.time()
runtime = 300

pin_num = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_num, GPIO.IN)
GPIO.add_event_detect(pin_num, GPIO.FALLING)


detected_times = []

while (time.time() - start_time < runtime):
    if GPIO.event_detected(pin_num):
        curr_time = time.time()
        detected_times.append(curr_time)
        print("Count at time: {:}".format(curr_time))

print("Over the span of 300 seconds, we measured {:} counts.".format(len(detected_times)))
