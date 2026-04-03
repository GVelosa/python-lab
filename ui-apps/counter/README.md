# Countdown Timer (Flet UI)

A simple graphical countdown timer built with Python.

The program allows the user to enter a number of seconds and then performs a countdown, updating the remaining time every second directly in the interface. When the countdown reaches zero, the button is re-enabled and the process can be started again.

---

## Concepts Used

- Variables
- While loops
- Conditional statements (`try`, `except`)
- User input handling
- Asynchronous programming (`async`, `await`)
- Time control with `asyncio.sleep()`
- Basic control flow
- UI state management (enable/disable button)
- Dynamic UI updates

---

## How It Works

1. The program asks the user to enter the number of seconds for the countdown.
2. If the input is not a valid number, an error message is displayed on the screen.
3. If the input is valid, the program starts a countdown using a `while` loop.
4. The start button is disabled during the countdown.
5. The remaining time is updated every second in the interface.
6. When the countdown reaches zero, the button is enabled again.