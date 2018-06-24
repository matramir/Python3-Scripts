# python3
# argvprint.py - a simple scrypt that i use sometimes to identify the sys argv when calling a
# python scrypt on the command line, useful when debugging scripts that use the sys.argv variable
# usage: python3 arvprint.py <extra arguments>
import sys
end = len(sys.argv) -1
print (str(len(sys.argv)))
for i in range(end):
    print ('sys.argv['+str(i)+'] = '+sys.argv[i])
