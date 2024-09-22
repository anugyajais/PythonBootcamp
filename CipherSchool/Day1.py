'''Imagine a fun game where you're challenged to guess a secret number. The computer selects a number between 1 and 100, and your task is to figure it out. With each guess, you'll receive hints to guide you.

What You’ll Build:

The Secret Number:
The game begins with the computer randomly selecting a number between 1 and 100. This is the secret number you'll be trying to guess.

Making Guesses:
You'll be prompted to guess a number between 1 and 100. If your input is outside that range or not a number, the game will remind you to try again.

Hints and Feedback:
If your guess is too low: "Too low! Try again."
If your guess is too high: "Too high! Try again."
If you guess correctly, you'll receive a congratulatory message along with the number of attempts.

Keep Guessing:
The game continues until you guess the correct number, so take your time and think carefully.

Ending the Game:
Once you've guessed the number, the game will end and let you know how many attempts it took.

Fun Extras:
To make it even better, handle any mix-ups in input (like letters instead of numbers) gracefully so you can focus on having fun.'''

import random

value = random.randint(1,100)

while(1):
    a= int(input("Make a guess for the secret number [Hint- 1-100]"))
    if a>value :
        print("Too high! Try again.")
    elif a<value:
        print("Too low! Try again.")
    elif value==a:
        print("YAYY! The number is ", a)
        break
        
        
       
        