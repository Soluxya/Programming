import random
from random import randint

def askname():
    global name
    print('Hello. What is your name?')
    name = input()
    return name

def defineNumber():
    global secretNumber
    askname()
    secretNumber = random.randint(1, 20)
    print("Well " + name + " I am thinking of a number between 1 and 20")
    return secretNumber


def gameLogic():
    defineNumber()
    for guessesTaken in range (1, 7):
        print("\n      Take a guess.")
        guess = int(input())
        if guess < secretNumber:
            print("your guess is too low")
        elif guess > secretNumber:
            print("your guess is too high")
        else:
            break
    if guess == secretNumber:
        print("\nGood job " + name + " you guessed my number: " + secretNumber)
    else:
        print("\nNope. The number i was thinking off was " + str(secretNumber))

def gameStart():
    gameLogic()

gameStart()