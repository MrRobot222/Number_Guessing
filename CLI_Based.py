#!/usr/bin/python3

import random

n = random.randrange(1,15)

guess = 0

print("\n\t    NUMBER GUESSING\n")
print("\t\tRULES\n")
print(" 1. You can Guess Any number between 1-15")
print(" 2. You have only five chances\n")
input("Press any key to start ")
print("\n")
    

while guess<5:
    guess_n = int(input("Please Enter your guess: "))
    guess = guess + 1
    if guess_n < n:
        print("Good try, but that's not correct")
        print("Your Guess was lesser")
    elif guess_n > n:
        print("Opps! Your guess was greater")
    else:
        print("BINGO")
        print(f"Your Guess is correct, the guess was ", n)
        break