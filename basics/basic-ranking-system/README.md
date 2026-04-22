# Ranking System (CLI)

A simple terminal-based ranking system built with Python.

The program stores a list of subjects with their respective scores and automatically generates a ranking based on those scores. The results are sorted from highest to lowest and displayed in the terminal with their corresponding positions.

---

## Concepts Used

- Dictionaries (`dict`)
- Tuples
- Sorting with `sorted()`
- Lambda functions
- Looping with `for`
- `enumerate()` for ranking positions
- String formatting (f-strings)
- Type hints (`dict[str, float | int]`)

---

## How It Works

1. A dictionary is defined with subjects as keys and their scores as values.
2. The dictionary is converted into a list of tuples using `.items()`.
3. The data is sorted using `sorted()` based on the score (value of each tuple).
4. A lambda function (`lambda item: item[1]`) is used to specify that sorting should be done by score.
5. The `reverse=True` parameter ensures the ranking is from highest to lowest.
6. The `enumerate()` function assigns a position to each item, starting from 1.
7. Each subject and its score are printed alongside its ranking position.
8. The final ranking is displayed in the terminal.
