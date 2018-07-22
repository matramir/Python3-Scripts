#! python3
# stopwatch.py - a simple stopwatch program
import time
#display program instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. \nPress Ctl-C to quit.')
input()
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 1
#start tracking lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone')
