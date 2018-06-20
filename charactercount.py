import pprint
print('Please enter message:')
msg=input()
count = {}
for character in msg.upper() :
  count.setdefault(character, 0)
  count[character] = count[character] +1
pprint.pprint(count)
