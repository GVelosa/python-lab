# Countdown Timer (CLI)

A simple terminal-based countdown timer built with Python.

The program asks the user to enter a number of seconds and then performs a countdown, updating the remaining time every second directly in the terminal. When the countdown reaches zero, a message is displayed.

---

## Concepts Used

- Variables
- While loops
- Conditional statements (`try`, `except`)
- User input handling
- Time control with `time.sleep()`
- Basic control flow
- String formatting (f-strings)

---

## How It Works

1. The program asks the user to enter the number of seconds for the countdown.
2. If the input is not a valid number, an error message is displayed.
3. If the input is valid, the program starts a countdown using a `while` loop.
4. The remaining time is updated every second in the terminal.
5. When the countdown reaches zero, the program displays "Time's up!"