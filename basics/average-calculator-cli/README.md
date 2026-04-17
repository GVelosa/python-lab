# Average Calculator (CLI)

A simple terminal-based average calculator built with Python.

The program allows the user to enter a list of numbers separated by spaces and calculates the average of those numbers. The result is displayed directly in the terminal. The program keeps running until the user decides to exit.

---

## Concepts Used

- Variables
- While loops
- Conditional statements (`if`, `break`, `continue`)
- User input handling
- Lists and list comprehension
- Error handling (`try`, `except`)
- Type conversion (`float`)
- Basic arithmetic operations

---

## How It Works

1. The program prompts the user to enter a list of numbers separated by spaces.
2. If the user presses Enter without typing anything, the program exits.
3. The input string is split into individual values.
4. The program attempts to convert each value into a number (`float`).
5. If the input is invalid (non-numeric), an error message is displayed.
6. If the input is valid but empty (e.g., only spaces), the program asks for at least one number.
7. The average is calculated by dividing the sum of the numbers by the total count.
8. The result is printed in the terminal.
9. The process repeats until the user exits.