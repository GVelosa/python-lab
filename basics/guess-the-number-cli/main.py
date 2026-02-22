import random
import os

os.system('cls')

print("Guess the number!")
print("I am thinking of a number between 1 and 100.")
print("------------------------------------------")

attempts = 0
randon_numb = random.randint(1, 100)
user_guess = int(input("To begin, enter positive integer: "))

while True:
    attempts += 1
    if user_guess < randon_numb:
        user_guess = int(input("Too Small, try again with a bigger number: "))   
    elif user_guess > randon_numb:
        user_guess = int(input("Too High, try again with a small number: "))     
    else:
        print("Congratulations! the number was:", randon_numb)
        print("You guessed in", attempts, "attempts.")
        break