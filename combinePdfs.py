#! python3
# combinePdfs.py - combines all the PDFs in the current working directory into a single pdf
import PyPDF2, os
#get all the pdf filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

#loop pdf filenames
for filename in pdfFiles:
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #loop for the pages of the pdf file
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfFileObj.close()
#save output
pdfOutput = open('combinedpdfs.pdf'.'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
