# Simple Navigation Bar

A small study project focused on learning how to implement **basic navigation between pages** using **Python** and the **Flet** framework.

The project demonstrates how to create a simple application structure with a **NavigationBar**, an **AppBar**, and dynamically changing content based on the selected navigation item.

> [!NOTE]  
> This project was created as a **learning exercise** to explore page navigation and basic application structure in Flet.

---

## Features

* Bottom **NavigationBar** with multiple destinations.
* Dynamic **content switching** based on selected navigation item.
* Modular **page structure**.
* Separation of **components and pages**.
* Simple **event-driven UI updates**.

---

## Technologies Used

| Technology | Description |
| :--- | :--- |
| [Python](https://www.python.org/) | Programming language used for the application logic. |
| [Flet](https://flet.dev/) | UI framework used to build the application interface. |

---

## Project Structure

The project is organized to separate **UI components** from **pages**, making the code easier to scale and maintain.

```
project/
│
├── main.py
│
├── components/
│   ├── navbar.py
│   └── appbar.py
│
└── pages/
    ├── home.py
    └── user.py
```

### Components

Reusable interface elements used across the application.

- **NavigationBar** – Handles page navigation.
- **AppBar** – Displays the main application header.

### Pages

Each page is encapsulated in its own function and returned as a Flet control.

- **Home Page**
- **User Page**

---

## Navigation Logic

The navigation works by listening to the `on_change` event from the **NavigationBar**.

When the selected index changes, the application updates the content displayed on the screen.

Example:

```python
def change_page(e):
    if page.navigation_bar.selected_index == 0:
        content.content = home
    elif page.navigation_bar.selected_index == 1:
        content.content = user

    page.update()
```

The content is wrapped in a **Container**, which allows the application to dynamically swap the page content without recreating the entire layout.

---

## Purpose of the Project

This repository focuses on learning how to:

* Implement **navigation between pages** in Flet.
* Structure a project with **separate components and pages**.
* Use **event-driven updates** to modify the UI.
* Build the foundation for **larger multi-page Flet applications**.

---

## Future Improvements

Possible improvements for future iterations:

* Implement **route-based navigation** using `page.go()`.
* Add more pages and features.
* Introduce **state management**.
* Improve layout responsiveness.
* Add more reusable components.

---

## Learning Focus

This project is part of a broader effort to practice:

* UI development with **Flet**
* **Component-based architecture**
* **Modular project organization**
* Building **scalable Python UI applications**