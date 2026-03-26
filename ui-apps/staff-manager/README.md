# Staff Manager

A Human Resources (HR) management system designed to streamline employee registration and role organization. This project was built to explore the synergy between **Object-Oriented Programming (OOP)** and modern UI development.

> [!IMPORTANT]  
> The primary goal of this project is to strengthen core OOP concepts—such as inheritance, abstraction, and encapsulation—while utilizing **Flet** to create a functional and responsive interface.

## Features
* **Role-Based Hierarchy:** Utilizes a base `Employee` class with specialized subclasses (Manager, Developer, Intern, etc.) to handle specific attributes and behaviors.
* **Interactive Registration:** A clean Flet-based form that adapts inputs according to the selected job role.
* **Polymorphic Logic:** Shared methods (like salary or bonus calculations) that behave differently depending on the employee's class.
* **Data Organization:** Structured management of personnel records within a corporate logic flow.

## Technologies Used

| Technology | Description |
| :--- | :--- |
| [Python](https://www.python.org/) | Programming language used for the core business logic and OOP architecture. |
| [Flet](https://flet.dev/) | UI Framework used to build the graphical interface using Flutter's engine. |

---

## What I Learned
By shifting from simple scripts to a class-based architecture, this project helped with:
* **Inheritance:** Reducing code redundancy by sharing common traits (Name, ID, Email) in a parent class.
* **Abstraction:** Creating template classes that shouldn't be instantiated directly, serving only as blueprints for roles.
* **Encapsulation:** Protecting sensitive employee data (like salaries) using private attributes and controlled access methods.
* **Componentization in Flet:** Breaking down the UI into reusable classes, making the interface as organized as the backend logic.