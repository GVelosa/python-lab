# Jo-Ken-Po with Flet

A classic Rock-Paper-Scissors game built in Python. This project marks my first steps with the **Flet** library, focusing on basic UI interactions, state updates, and simple game logic.

> [!NOTE]  
> This was my introductory project to Flet, used to explore how components and event handlers work in a real-time interface.

## Features
* **Interactive UI:** Clean and centered layout using Flet's `Row` and `Column` containers.
* **Randomized AI:** A bot that makes a random selection every time the player clicks a button.
* **Visual Feedback:** Results are displayed with dynamic colors (Green for win, Yellow for draw, Red for loss).
* **Icon-based Gameplay:** Uses Material Design icons for intuitive player choices.

## Technologies Used

| Technology | Description |
| :--- | :--- |
| [Python](https://www.python.org/) | Programming language for the core game logic. |
| [Flet](https://flet.dev/) | UI Framework used to build the graphical interface. |
| [Random (Standard Lib)](https://docs.python.org/3/library/random.html) | Python module used to generate the bot's moves. |

---

## What I Learned
Being my first Flet project, it helped with:
* **Event Handlers:** Using `on_click` to trigger functions.
* **Component Updates:** Understanding the importance of `.update()` to reflect changes on the screen.
* **Conditional Styling:** Changing text colors and icons dynamically based on game outcomes.

## Future Improvements
* Add a score counter for both player and bot.
