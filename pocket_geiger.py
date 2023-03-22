import RPi.GPIO as GPIO
import time

start_time = time.time()
runtime_minutes = 5

pin_num = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_num, GPIO.IN)
GPIO.add_event_detect(pin_num, GPIO.FALLING)


cpm = []
time_stamps = []
count = 0
last_run = 0

while ((time.time() - start_time) < runtime_minutes * 60):

    # Set time for the run of this loop
    last_run = (time.time() - start_time)%60
    
    # Check for an event
    time_out = int((60 - last_run))*1000
    print(last_run, time_out)
    channel = GPIO.wait_for_edge(pin_num, GPIO.FALLING, timeout = time_out)
    if (channel is None):
        cpm.append(count)
        print("There were {:} counts in the last minute.".format(count))
        count = 0
    else:
        time_stamps.append(time.time())
        print("Count at time: {:}".format(time_stamps[-1]))
        count += 1
        
# Make sure we have actually recorded all the data, if it did not register the final minute ending, append leftover data
if(len(cpm) != runtime_minutes):
    cpm.append(count)
    
print("Over the span of {} minutes, we measured {:} counts.".format(runtime_minutes, len(time_stamps)))
