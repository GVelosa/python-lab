# Staff Manager

A Human Resources (HR) management system designed to streamline employee registration and role organization. This project was built to explore the synergy between **Object-Oriented Programming (OOP)**, relational databases, and modern UI development.

> [!IMPORTANT]
> The primary goal of this project is to strengthen core OOP concepts—such as inheritance, abstraction, and encapsulation—while utilizing **Flet** to create a functional and responsive interface, alongside **SQLite** for structured data persistence.

---

## Features

* **User Authentication (Basic):** Platform user registration with validation and database persistence.
* **Role-Based Hierarchy:** Utilizes a base `Employee` class with specialized subclasses (Manager, Developer, Intern, etc.) to handle specific attributes and behaviors.
* **Interactive Registration:** A clean Flet-based form that adapts inputs according to the selected job role.
* **Polymorphic Logic:** Shared methods (like salary or bonus calculations) that behave differently depending on the employee's class.
* **Relational Data Modeling:** Employees are linked to departments and job roles using foreign keys, ensuring consistency and scalability.
* **Data Organization:** Structured management of personnel records following real-world HR relationships (employee → manager → department).

---

## Technologies Used

| Technology                        | Description                                                                    |
| :-------------------------------- | :----------------------------------------------------------------------------- |
| [Python](https://www.python.org/) | Core language used for business logic, OOP structure, and backend operations.  |
| [Flet](https://flet.dev/)         | UI framework used to build a responsive graphical interface.                   |
| SQLite                            | Lightweight relational database used for persistent storage and data modeling. |

---

## Database Design

The project uses a **normalized relational database structure** to ensure data consistency and scalability.

### Main Tables:

* **users:** Stores platform authentication data
* **employees:** Stores employee information and hierarchical relationships
* **departments:** Defines organizational units
* **job_titles:** Standardizes roles across the system

### Key Concepts Applied:

* **Normalization:** Avoids redundancy by separating entities into dedicated tables
* **Foreign Keys:** Ensures referential integrity between employees, departments, and roles
* **Self-relationship:** Employees can reference other employees as managers (`manager_id`)
* **Data Consistency:** IDs are used instead of raw text to prevent duplication and typos

---

## What I Learned

By evolving from simple scripts into a structured application, this project helped reinforce:

### 🧠 OOP Concepts

* **Inheritance:** Reducing code redundancy by sharing common traits (Name, ID, Email) in a parent class.
* **Abstraction:** Creating template classes that shouldn't be instantiated directly, serving only as blueprints for roles.
* **Encapsulation:** Protecting sensitive employee data (like salaries) using controlled access patterns.
* **Polymorphism:** Implementing flexible behaviors depending on employee roles.

### 🗄️ Database & Backend Concepts

* **Relational Modeling:** Designing structured relationships between entities like employees, departments, and roles.
* **Data Integrity:** Using constraints (`UNIQUE`, `CHECK`, `FOREIGN KEY`) to ensure reliable data.
* **Separation of Concerns:** Keeping UI, business logic, and database operations independent.
* **Scalability Thinking:** Structuring the database in a way that allows future expansion without major refactoring.

### 🎨 UI Architecture

* **Componentization in Flet:** Breaking down the UI into reusable components for maintainability and clarity.

---

## Future Improvements

* Implement password hashing (security enhancement)
* Add login system and session control
* Create dashboards with employee analytics
* Introduce performance review history tracking
* Improve validation and error handling in UI

---
