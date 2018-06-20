import send2trash, os
isPath = False
while isPath ==False:
    print ("Please enter the filepath that you want to send to the recycle bin:")
    path = input()
    isPath = os.path.exists(path)
send2trash.send2trash(path)
print ('The filepath \" '+ path +' \" was sent to the recycle bin.')
