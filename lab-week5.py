import sys
import random
import time

runtime = int(sys.argv[1]) #s, input from terminal
i = 0

while i < runtime:

    info = (time.time(), \
        random.random())
    print(info)

    time.sleep(1)
    i += 1