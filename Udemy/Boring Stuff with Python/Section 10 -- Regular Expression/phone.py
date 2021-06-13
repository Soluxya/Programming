import re

message = 'Call me 415-555-1011 tommorow, or at 415-555-9999 for my office line'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Call me 415-555-1011 tommorow, or at 415-555-9999 for my office line'))














# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False #not number-sized
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False # no area code
#     if text[3] != '-':
#         return False # missing dash
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False # no four to six digits   
#     if text[7] != '-':
#         return False # missing second dash
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False # no eight to twelve digits   
#     return True

# message = 'Call me 415-555-1011 tommorow, or at 415-555-9999 for my office line'
# foundNumber = False
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found ' + chunk)
#         foundNumber = True
# if not foundNumber:
#     print('Could not find any phone numbers')