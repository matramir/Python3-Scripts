# python3
#collatz.py
def collatz(number):
    try:
        if ((number%2)==0):
            result = number // 2
            print (str(number)+' // 2 = ' +str(result))
        else:
            result = 3 * number + 1
            print ('3 * '+str(number)+' + 1 = '+ str(result))
        return result
    except ValueError:
        print ('Please enter proper value type (integer)')
print('Please enter a  number: ')
value = collatz(int(input()))
while (value!=1):
    value = collatz(value)
