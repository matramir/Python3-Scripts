#! Python3
# csvPrinter - prints on the terminal the contents of a csv file
# usage script comand must contain the relative filepath to the pwd
import sys, os, csv
if (len(sys.argv)==2):
    try:
        filePath = os.path.join(os.path.abspath('.'), sys.argv[1])
        eFile = open(filePath)
        eReader = csv.reader(eFile)
        eDocument = list(eReader)
        for element in eDocument:
            print(element)
    except:
        print('Something went wrong please check the file path of your csv file.')
else:
    print('Wrong amount of arguments when calling the script. Must contain relative filepath to the pwd as the usage details.')
