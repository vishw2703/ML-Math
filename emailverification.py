import pyperclip, re

#for phoneno
phoneRegex = re.compile(r'''((\d{10}))''', re.VERBOSE)

#for emailid

emailRegex = re.compile(r'''([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
    matches.append(groups[0])
    
for groups in emailRegex.findall(text):
   phoneNum = '-'.join([groups[0]])
   matches.append(phoneNum)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard:')
    print('\n'.join(matches))

else:
    print('No phone number or email found')

