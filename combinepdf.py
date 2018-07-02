#! python3
# combinepdf.py - a simple script that combines the contents of two pdf files
import os, PyPDF2, sys
def pagewriter(pwriter ,preader):
    for  pageNum in range(preader.numPages):
        page = preader.getPage(pageNum)
        pwriter.addPage(page)

if length(sys.argv) == 3:
    try:
        # path of both files
        path1 = str(sys.argv[1])
        path2 = str(sys.argv[2])
        # open the files
        pdf1File = open(path1, 'rb')
        pdf2File = open(path2, 'rb')
        # create reader objects
        reader1 = PyPDF2.PdfFileReader(pdf1File)
        reader2 = PyPDF2.PdfFileReader(pdf2File)
        # create writer object for resulting file
        writer = PyPDF2.PdfFileWriter()
        # use pagewriter function
        pagewriter(reader1, writer)
        pagewriter(reader2, writer)
        outputFile = open('combined.pdf', 'wb')
        writer.write(outputFile)
        outputFile.close()
        pdf1File.close()
        pdf2File.close()
    except:
        print('error')
else:
    print('Enter the proper ammount of arguments.')
