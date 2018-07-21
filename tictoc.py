#! python3
# tictoc.py - script that prints tic toc depending on the second argv
import sys, time

def ticmsg(s):
    for val in range(1,(s+1)):
        if (val % 2) == 0:
            print('toc')
        else:
            print('tic')
        time.sleep(1)
try:
    seconds = int(sys.argv[1])
    ticmsg(seconds)
except:
    print('Something went wrong')
    sys.exit()
