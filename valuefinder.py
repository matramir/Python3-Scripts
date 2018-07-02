#! python3
#valuefinder.py - returns the value from a excel file
import sys, os, openpyxl
def getValue(name ,sheetName, columnN , rowN):
    filePath = os.path.join(os.path.abspath('.'), (str(name)+'.xlsx'))
    wb = openpyxl.load_workbook(filePath)
    sheet = wb.get_sheet_by_name(sheetName)
    value = wb[sheetName].cell(row=int(rowN), column=int(columnN)).value
    return value
try:
    print(str(getValue(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] )))
except:
    print('error')
