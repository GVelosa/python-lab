import os

os.system('cls')

print("Factorial Calculator!")
print("--------------------")

number = int(input("Enter a non-negative integer: "))
factorial = 1


if number < 0:
        print("Please, input a whole number not negative")
else:        
    for num in range(1, number + 1):
        factorial = factorial * num

print(f"The factorial of {number} is: {factorial}.")