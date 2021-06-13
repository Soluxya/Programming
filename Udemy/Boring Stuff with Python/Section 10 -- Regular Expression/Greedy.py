

# Create Regex for phone numbers; Creat regex for email adresses

# Get the text off the clibboard; Extract the email/phone from this text

# Copy the extracted emails/phone numbers to the cliboard

import re, pyperclip
from re import VERBOSE

def question():
    """
    This explains the usage of the '?' operand on Regex functions.
    """
    batRegex = re.compile(r'Bat(wo)?man')
    mo = batRegex.search('The Adventures of Batman')
    print(mo.group())
    mo = batRegex.search('The Adventures of Batwoman')
    print(mo.group())
    pass

def starshape():
    """
    This function explains the usage of the '*' operand on Regex functions.
    """
    batRegex = re.compile(r'Bat(wo)*man')
    mo = batRegex.search('The Adventures of Batman')
    print(mo.group())
    mo = batRegex.search('The Adventures of Batwoman')
    print(mo.group())
    mo = batRegex.search('The Adventures of Batwowowoman')
    print(mo.group())
    pass

def plus():
    """
    This function explains the usage of the '+' operand on Regex functions.
    """
    batRegex = re.compile(r'Bat(wo)+man')
    print(batRegex.search('The adventures of Batman') == None)
    print(batRegex.search('The adventures of Batwoman'))
    print(batRegex.search('The adventures of Batwowowoman'))
    pass


def email_phone():
    """
    Create Regex for phone numbers; Creat regex for email adresses

    Get the text off the clibboard; Extract the email/phone from this text

    Copy the extracted emails/phone numbers to the cliboard
    """
    phoneRegex = re.compile(
        r'''
        (
        (((\d\d\d) | (\(\d\d\d)))? # area code (optional)
        (\s|-)                     # first separator
        \d\d\d                     # first 3 digits
        -                          # second separator
        \d\d\d\d                   # last 4 digitis
        (((ext(\.)?\s)|x)          # extension (optional)
        (\d{2,5}))?                # extension (optional)
        )
        ''', 
        re.VERBOSE)
    emailRegex = re.compile(
        r'''
        [a-zA-Z0-9_.+]+            # name part
        @                          # at symbol 
        [a-zA-Z0-9_.+]+            # domain name part         
        ''', 
        re.VERBOSE)
    
    
    text = pyperclip.paste()
    extractedPhone = phoneRegex.findall(text)
    extractedEmail = emailRegex.findall(text)
    allPhoneNumbers = []
    for i in extractedPhone:
        allPhoneNumbers.append(i[0])
    results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
    pyperclip.copy(results)

# question()
# starshape()
# plus()
email_phone()

