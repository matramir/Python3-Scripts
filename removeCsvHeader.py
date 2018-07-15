#! python3
# removeCsvHeader.py - removes the header from all csv files in the pwd
# working directory
import  csv, os
os.makedirs('headerRemoved', exist_ok=True)
#loop through every file in the current working directory
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue #skips file
    print ("Removing header from " + csvFilename+ '...')
    #read csvFile
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj =csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num  == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()
    #write csvFile
    print('writing output file for '+ csvFilename + ' in ' + os.path.join(os.path.abspath('.'),'headerRemoved',csvFilename) )
    csvFileObj = open(os.path.join('headerRemoved, csvFilename'), 'w', newline ='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
