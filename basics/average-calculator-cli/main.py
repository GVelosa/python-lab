import os

os.system('cls')

numbers_str = []

print("Enter a list of numbers separated by spaces")
print("If you want to exit, press enter!")
print("---------------------------------------------------------------")


while True:
    initial_numbers = input("Enter a number: ")
    
    if initial_numbers.lower() == "":
        break

    numbers_str = initial_numbers.split()
    if not numbers_str:
        print("Please enter at least one number.")
        continue
    
    try:
        number_list = [float(num) for num in numbers_str]
        average = sum(number_list) / len(number_list)
        print("Average is", average)

    except ValueError:
        print("Invalid input! Please enter only numbers.")