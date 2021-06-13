import random
import sys
x = random.randint(1, 10)
print(x)
print("Goodbye friend")
import pyperclip
pyperclip.copy("Hello World!")
x = pyperclip.paste()
print(x)
help(x)